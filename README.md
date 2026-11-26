# CampusHelp — University Student Service Request Portal

Project Management Assignment · COSC 3500 IT Project Management · Webster University

CampusHelp is a proposed web-based system where students submit service requests (IT support, classroom maintenance, library assistance, administrative services) and follow them until they are resolved. This repository holds the project-management documents, the wireframes, a clickable prototype and the evidence of planning, execution, monitoring and closure.

## Team

| Full name | Student ID | GitHub | Role |
|---|---|---|---|
| Diyorjon Sobirov | _(add)_ | [@Diyorbek200614](https://github.com/Diyorbek200614) | Project Manager (A), Business Analyst & Designer (B), Quality & Risk Coordinator (C) |

This is an individual submission: the lecturer allowed the assignment to be completed alone, so one student covers all three roles. Documents still state the role responsible for each task (A, B, C) so the division of work stays visible.

## Links

- Project Board: <https://github.com/users/Diyorbek200614/projects/2>
- Milestones: <https://github.com/Diyorbek200614/CampusHelp-Team01/milestones>
- Issues: <https://github.com/Diyorbek200614/CampusHelp-Team01/issues?q=is%3Aissue>
- Pull Requests: <https://github.com/Diyorbek200614/CampusHelp-Team01/pulls?q=is%3Apr>

## Documents

| Document | File | Issue |
|---|---|---|
| Project charter | [docs/project-charter.md](docs/project-charter.md) | T01 |
| Requirements & stakeholders | [docs/requirements.md](docs/requirements.md) | T02 |
| Scope statement & WBS | [docs/wbs.md](docs/wbs.md) | T03 |
| Schedule, dependencies & budget | [docs/schedule-and-budget.md](docs/schedule-and-budget.md) | T04 |
| Initial wireframes | [docs/wireframes.md](docs/wireframes.md) | T05 |
| Risk register | [docs/risk-register.md](docs/risk-register.md) | T06 |
| Quality plan | [docs/quality-plan.md](docs/quality-plan.md) | T06 |
| Student request interface | [prototype/index.html](prototype/index.html), [prototype/track.html](prototype/track.html) | T07 |
| Administrator dashboard | [prototype/admin.html](prototype/admin.html) | T08 |
| Test cases & results | [docs/test-cases.md](docs/test-cases.md) | T09 |
| Change request | docs/change-request.md | T10 |
| Verification report | docs/verification-report.md | T11 |
| Closure report & final PDF | docs/closure-report.md | T12 |
| Progress checkpoints (Day 2, 5, 8) | docs/monitoring/ | — |

## Running the prototype

Download the repository and open `prototype/index.html` in a browser, or serve the folder locally:

```
python -m http.server 5610 --directory prototype
```

Then open <http://localhost:5610>. Data is stored only in the browser (simulated back end); **Admin → Reset sample data** restores the sample requests.

## Workflow

- Every task is a GitHub Issue (T01–T12) with objective, deliverable, acceptance criteria, dependency, estimate and evidence.
- Every change reaches `main` through a Pull Request that references its Issue.
- An Issue is closed only after its deliverable is merged and checked against the Definition of Done in the quality plan.

## Use of AI

AI assistance (Claude, Anthropic) was used to help draft documents and the prototype, as permitted by the lecturer. The student reviewed, edited and is accountable for all content.
