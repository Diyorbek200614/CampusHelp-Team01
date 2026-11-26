"""Build CampusHelp_Team01_FinalReport.pdf from the repository documents and live GitHub data.

    uv run --no-project --with markdown python report/build_report.py

Needs: GitHub CLI logged in as the repo owner, Google Chrome (headless print to PDF).
"""
from __future__ import annotations

import html
import json
import os
import re
import subprocess
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT_HTML = ROOT / "report" / "report.html"
OUT_PDF = ROOT / "CampusHelp_Team01_FinalReport.pdf"
SHOTS = ROOT / "report" / "screenshots"
OWNER = "Diyorbek200614"
REPO = f"{OWNER}/CampusHelp-Team01"
REPO_URL = f"https://github.com/{REPO}"
BOARD_URL = f"https://github.com/users/{OWNER}/projects/2"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def gh_json(*args: str):
    env = dict(os.environ)
    if "GH_TOKEN" not in env:
        env["GH_TOKEN"] = subprocess.check_output(["gh", "auth", "token", "--user", OWNER], text=True).strip()
    out = subprocess.check_output(["gh", *args], text=True, encoding="utf-8", env=env)
    return json.loads(out)


def md(path: str, drop_title: bool = True, shift: int = 1) -> str:
    text = (ROOT / path).read_text(encoding="utf-8")
    if drop_title:
        text = re.sub(r"\A# .*\n", "", text)
    # metadata table at the top is kept; shift headings so they nest under the report section
    text = re.sub(r"^(#{2,5}) ", lambda m: "#" * (len(m.group(1)) + shift) + " ", text, flags=re.M)
    # mermaid blocks -> <pre class="mermaid">
    text = re.sub(r"```mermaid\n(.*?)```", lambda m: f'<pre class="mermaid">{html.escape(m.group(1))}</pre>', text, flags=re.S)
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    # relative repo links -> absolute GitHub links (working links in the PDF)
    base = f"{REPO_URL}/blob/main/{Path(path).parent.as_posix()}/"
    body = re.sub(r'href="(?!https?:|#|mailto:)([^"]+)"', lambda m: f'href="{base}{m.group(1)}"', body)
    return body


def shot(name: str, caption: str) -> str:
    p = SHOTS / name
    if not p.exists():
        return f'<p class="missing">[Screenshot not available: {html.escape(caption)}]</p>'
    return f'<figure><img src="{p.as_uri()}"><figcaption>{html.escape(caption)}</figcaption></figure>'


def link(url: str, text: str | None = None) -> str:
    return f'<a href="{url}">{html.escape(text or url)}</a>'


def issues_table() -> str:
    data = gh_json("issue", "list", "--repo", REPO, "--state", "all", "--limit", "100",
                   "--json", "number,title,state,labels,milestone,assignees,closedAt")
    rows = []
    for i in sorted(data, key=lambda x: x["number"]):
        rows.append(
            f"<tr><td>{link(f'{REPO_URL}/issues/{i['number']}', '#' + str(i['number']))}</td>"
            f"<td>{html.escape(i['title'])}</td><td>{', '.join(l['name'] for l in i['labels'])}</td>"
            f"<td>{html.escape((i.get('milestone') or {}).get('title', ''))}</td>"
            f"<td>{', '.join(a['login'] for a in i['assignees'])}</td><td>{i['state'].title()}</td></tr>")
    return ("<table><thead><tr><th>Issue</th><th>Title</th><th>Labels</th><th>Milestone</th><th>Assignee</th>"
            "<th>State</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table>")


def board_table() -> str:
    data = gh_json("project", "item-list", "2", "--owner", OWNER, "--format", "json", "--limit", "100")["items"]
    rows = []
    for it in sorted(data, key=lambda x: x["content"].get("number", 0)):
        c = it["content"]
        rows.append(
            f"<tr><td>#{c.get('number')}</td><td>{html.escape(it.get('title', ''))}</td><td>{it.get('status', '')}</td>"
            f"<td>{it.get('priority', '')}</td><td>{it.get('estimated Hours', '')}</td><td>{it.get('actual Hours', '')}</td>"
            f"<td>{it.get('start Date', '')}</td><td>{it.get('due Date', '')}</td></tr>")
    return ("<table><thead><tr><th>#</th><th>Item</th><th>Status</th><th>Priority</th><th>Est. h</th><th>Actual h</th>"
            "<th>Start</th><th>Due</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table>")


def milestones_table() -> str:
    env_args = ["api", f"repos/{REPO}/milestones?state=all"]
    data = gh_json(*env_args)
    rows = "".join(
        f"<tr><td>{link(m['html_url'], m['title'])}</td><td>{html.escape(m['description'] or '')}</td>"
        f"<td>{(m['due_on'] or '')[:10]}</td><td>{m['closed_issues']}/{m['closed_issues'] + m['open_issues']}</td>"
        f"<td>{m['state'].title()}</td></tr>" for m in sorted(data, key=lambda m: m["number"]))
    return ("<table><thead><tr><th>Milestone</th><th>Description</th><th>Due</th><th>Closed issues</th><th>State</th>"
            "</tr></thead><tbody>" + rows + "</tbody></table>")


def prs_table() -> str:
    data = gh_json("pr", "list", "--repo", REPO, "--state", "all", "--limit", "100",
                   "--json", "number,title,headRefName,state,mergedAt,comments,body")
    rows = []
    for p in sorted(data, key=lambda x: x["number"]):
        refs = ", ".join(sorted(set(re.findall(r"(?:Closes|Refs) #(\d+)", p["body"] or ""))))
        rows.append(
            f"<tr><td>{link(f'{REPO_URL}/pull/{p['number']}', '#' + str(p['number']))}</td><td>{html.escape(p['title'])}</td>"
            f"<td><code>{html.escape(p['headRefName'])}</code></td><td>{('#' + refs.replace(', ', ', #')) if refs else ''}</td>"
            f"<td>{len(p['comments'])}</td><td>{p['state'].title()} {(p['mergedAt'] or '')[:16].replace('T', ' ')}</td></tr>")
    return ("<table><thead><tr><th>PR</th><th>Title</th><th>Branch</th><th>Issue</th><th>Review comments</th>"
            "<th>State (UTC)</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table>")


def build() -> None:
    S = []
    add = S.append
    add(f"""<section class="cover">
<h1>CampusHelp</h1>
<p class="subtitle">University Student Service Request Portal<br>GitHub-Based Project Management Assignment — Final Report</p>
<table class="meta">
<tr><th>Course</th><td>COSC 3500 IT Project Management</td></tr>
<tr><th>Institution</th><td>Webster University</td></tr>
<tr><th>Team</th><td>Team01 (individual submission)</td></tr>
<tr><th>Student</th><td>Diyorjon Sobirov</td></tr>
<tr><th>Student ID</th><td>4283260</td></tr>
<tr><th>GitHub</th><td>{link('https://github.com/' + OWNER, '@' + OWNER)}</td></tr>
<tr><th>Roles</th><td>Project Manager (A), Business Analyst &amp; Designer (B), Quality &amp; Risk Coordinator (C)</td></tr>
<tr><th>Repository</th><td>{link(REPO_URL)}</td></tr>
<tr><th>Project Board</th><td>{link(BOARD_URL)}</td></tr>
<tr><th>Date</th><td>26 November 2026</td></tr>
</table>
</section>""")

    add('<section><h1>Contents</h1><ol class="toc">' + "".join(f"<li>{t}</li>" for t in [
        "Project overview", "Team structure", "Project charter", "Work Breakdown Structure", "Schedule and budget",
        "Milestones", "GitHub Issues", "Project Board", "Collaboration", "Risk and change", "Testing",
        "Monitoring", "Closure", "References"]) + "</ol></section>")

    add(f"""<section><h1>1. Project overview</h1>
<h2>Problem statement</h2>
<p>A university receives student requests for IT support, classroom maintenance, library assistance and administrative services through e-mails and paper forms. Requests have no ID and no owner, students cannot see their progress, and the university cannot measure the service.</p>
<h2>Objectives</h2>
<ul><li>Plan and demonstrate CampusHelp, a centralized web portal where students submit requests and track them by a unique ID.</li>
<li>Cover all six proposed features: submission, categories &amp; priorities, tracking ID, administrator assignment, status updates, dashboard.</li>
<li>Manage the project end-to-end in GitHub: Issues, milestones, labels, Project Board, Pull Requests, risk and change control, monitoring and closure.</li></ul>
{shot('repo-home.png', 'Repository home page — ' + REPO_URL)}
</section>""")

    add(f"""<section><h1>2. Team structure</h1>
<table><thead><tr><th>Full name</th><th>Student ID</th><th>GitHub</th><th>Role(s)</th><th>Owned tasks</th></tr></thead>
<tbody><tr><td>Diyorjon Sobirov</td><td>4283260</td><td>{link('https://github.com/' + OWNER, OWNER)}</td>
<td>A – Project Manager<br>B – Business Analyst &amp; Designer<br>C – Quality &amp; Risk Coordinator</td><td>T01–T12 (12)</td></tr></tbody></table>
<table><thead><tr><th>Role</th><th>Responsibilities</th><th>Tasks</th></tr></thead><tbody>
<tr><td>A – Project Manager</td><td>Charter, schedule, milestones, progress monitoring, change control</td><td>T01, T04, T08, T10</td></tr>
<tr><td>B – Business Analyst &amp; Designer</td><td>Requirements, stakeholders, wireframes, prototype, final report</td><td>T02, T05, T07, T12</td></tr>
<tr><td>C – Quality &amp; Risk Coordinator</td><td>WBS, risk register, test cases, quality assurance, issue tracking</td><td>T03, T06, T09, T11</td></tr>
</tbody></table>
<p><b>Deviation:</b> the assignment specifies three students. The lecturer allowed an individual submission, so one student held all three roles. The role responsible for each task is still recorded in every document and Pull Request.</p>
{shot('collaborators.png', 'Repository access (Settings → Collaborators)')}
</section>""")

    add(f"<section><h1>3. Project charter</h1>{md('docs/project-charter.md')}"
        f"<h2>Requirements and stakeholders (T02)</h2>{md('docs/requirements.md', shift=2)}</section>")
    add(f"<section><h1>4. Work Breakdown Structure</h1>{md('docs/wbs.md')}</section>")
    add(f"<section><h1>5. Schedule and budget</h1>{md('docs/schedule-and-budget.md')}</section>")
    add(f"<section><h1>6. Milestones</h1>{milestones_table()}{shot('milestones.png', 'GitHub milestones with due dates and progress')}</section>")
    add(f"<section><h1>7. GitHub Issues</h1><p>All Issues: {link(REPO_URL + '/issues?q=is%3Aissue')}</p>{issues_table()}"
        f"{shot('labels.png', 'Labels')}{shot('issues.png', 'Issue list')}{shot('issue-example.png', 'Example Issue (T07) with mandatory description format')}</section>")
    add(f"""<section><h1>8. Project Board</h1><p>Board: {link(BOARD_URL)}</p>{board_table()}
{shot('board-mid.png', 'Board view — intermediate state (checkpoint 3: T01–T10 Done, T11–T12 Todo)')}
{shot('board-final.png', 'Board view — final state (all tasks Done)')}
{shot('table-view.png', 'Table view — owner, priority, estimated/actual hours, dates')}
{shot('roadmap-view.png', 'Roadmap view — planned start and due dates')}
<p class="small">The initial (all-Todo) board state was not captured before work began; see Closure → limitations.</p></section>""")
    add(f"""<section><h1>9. Collaboration</h1>
<p>Every deliverable reached <code>main</code> through a branch and a Pull Request that references its Issue; each PR has a review comment checked against the Issue's acceptance criteria. Because this is an individual submission, reviews are written from the reviewing role (A, B or C) by the same student.</p>
<p>Pull Requests: {link(REPO_URL + '/pulls?q=is%3Apr')} · Commits: {link(REPO_URL + '/commits/main')}</p>
{prs_table()}{shot('pull-requests.png', 'Merged Pull Requests')}{shot('pr-review.png', 'Example Pull Request with review comment')}</section>""")
    add(f"<section><h1>10. Risk and change</h1><h2>Risk register (T06)</h2>{md('docs/risk-register.md', shift=1)}"
        f"<h2>Quality plan (T06)</h2>{md('docs/quality-plan.md', shift=1)}"
        f"<h2>Change request CR-01 (T10)</h2>{md('docs/change-request.md', shift=1)}</section>")
    add(f"<section><h1>11. Testing</h1>{md('docs/test-cases.md')}"
        f"{shot('proto-form.png', 'Prototype — request form with validation')}{shot('proto-confirm.png', 'Prototype — confirmation with request ID')}"
        f"{shot('proto-track.png', 'Prototype — tracking page')}{shot('proto-admin.png', 'Prototype — administrator dashboard')}</section>")
    add("<section><h1>12. Monitoring</h1>"
        f"<p>Status summaries posted in GitHub: {link(REPO_URL + '/issues/26')}</p>"
        + "".join(f"<h2>Checkpoint {n}</h2>{md(f'docs/monitoring/checkpoint-{n}.md', shift=1)}" for n in (1, 2, 3))
        + "</section>")
    add(f"<section><h1>13. Closure</h1><h2>Final verification (T11)</h2>{md('docs/verification-report.md', shift=1)}"
        f"<h2>Closure report (T12)</h2>{md('docs/closure-report.md', shift=1)}</section>")
    refs = [
        ("Repository", REPO_URL), ("Project Board", BOARD_URL), ("Milestones", REPO_URL + "/milestones?state=all"),
        ("Issues", REPO_URL + "/issues?q=is%3Aissue"), ("Pull Requests", REPO_URL + "/pulls?q=is%3Apr"),
        ("Status reports", REPO_URL + "/issues/26"), ("Change request CR-01", REPO_URL + "/issues/24"),
        ("Documents folder", REPO_URL + "/tree/main/docs"), ("Prototype source", REPO_URL + "/tree/main/prototype"),
        ("GitHub Docs — About Projects", "https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects"),
        ("GitHub Docs — About milestones", "https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones"),
        ("GitHub Docs — About pull requests", "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests"),
        ("PMI, A Guide to the Project Management Body of Knowledge (PMBOK Guide), 7th ed., 2021", None),
    ]
    add("<section><h1>14. References</h1><ol>" + "".join(
        f"<li>{html.escape(t)}{': ' + link(u) if u else ''}</li>" for t, u in refs) + "</ol></section>")

    css = """
    @page { size: A4; margin: 16mm 14mm; }
    body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10pt; color: #1d2433; line-height: 1.45; }
    section { page-break-before: always; }
    section.cover { page-break-before: avoid; text-align: left; padding-top: 40mm; }
    .cover h1 { font-size: 34pt; color: #1f5fbf; margin: 0; }
    .subtitle { font-size: 14pt; color: #5b6475; margin: 6px 0 24px; }
    h1 { font-size: 17pt; color: #1f5fbf; border-bottom: 2px solid #1f5fbf; padding-bottom: 4px; }
    h2 { font-size: 13pt; margin-top: 18px; } h3 { font-size: 11pt; } h4 { font-size: 10pt; }
    table { border-collapse: collapse; width: 100%; margin: 8px 0 12px; font-size: 8.6pt; page-break-inside: auto; }
    tr { page-break-inside: avoid; }
    th, td { border: 1px solid #cfd5e2; padding: 4px 6px; text-align: left; vertical-align: top; }
    th { background: #eef2fa; }
    table.meta { width: auto; font-size: 10.5pt; } table.meta th { width: 120px; }
    pre { background: #f6f8fa; padding: 8px; font-size: 8pt; white-space: pre-wrap; border-radius: 4px; }
    pre.mermaid { background: none; text-align: center; }
    code { font-size: 8.6pt; background: #f2f4f8; padding: 0 3px; border-radius: 3px; }
    a { color: #1f5fbf; word-break: break-all; }
    figure { margin: 10px 0; page-break-inside: avoid; } figure img { max-width: 100%; border: 1px solid #cfd5e2; }
    figcaption { font-size: 8.5pt; color: #5b6475; margin-top: 3px; }
    .missing { color: #b42318; font-style: italic; } .small { font-size: 8.5pt; color: #5b6475; }
    blockquote { border-left: 3px solid #1f5fbf; margin: 8px 0; padding: 2px 10px; color: #344054; }
    """
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>CampusHelp_Team01_FinalReport</title>
<style>{css}</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{startOnLoad: true, theme: 'neutral', securityLevel: 'loose', gantt: {{useWidth: 900}}}});</script>
</head><body>{''.join(S)}</body></html>"""
    OUT_HTML.write_text(doc, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
                    "--virtual-time-budget=15000", f"--print-to-pdf={OUT_PDF}", OUT_HTML.as_uri()], check=True)
    print("PDF:", OUT_PDF, OUT_PDF.stat().st_size, "bytes")


if __name__ == "__main__":
    build()
