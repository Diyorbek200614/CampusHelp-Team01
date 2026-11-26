# Quality Plan — CampusHelp

| | |
|---|---|
| **Document ID** | QA-03 (Issue T06) |
| **Version** | 1.0 |
| **Date** | 26 November 2026 |
| **Role** | Quality & Risk Coordinator (Student C) |

## 1. Quality objectives

| Objective | Metric | Target |
|---|---|---|
| Complete coverage of the proposed system | Features represented in requirements and prototype | 6 of 6 |
| Correct prototype behaviour | Mandatory test cases passed | ≥ 90 %, all failures documented |
| Traceable work | Closed Issues with an evidence link (document or PR) | 100 % |
| Reviewed work | Pull Requests reviewed before merge | 100 % |
| Usable design | Request submitted by a first-time user | < 2 minutes |

## 2. Quality standards

- **Documents:** Markdown in `docs/`, each with ID, version, date and owner role; tables for structured data; diagrams in Mermaid so they render on GitHub.
- **Prototype:** plain HTML / CSS / JavaScript, no external libraries; works offline by opening the file; usable at 360 px and 1280 px width; labelled fields; errors shown as text.
- **GitHub:** every Issue follows the mandatory format (Objective, Description, Deliverable, Acceptance criteria, Dependency, Estimated effort, Completion evidence); every change to `main` arrives through a Pull Request that references its Issue.

## 3. Quality assurance activities (process)

| Activity | When | Responsible |
|---|---|---|
| Pull Request review against the Issue's acceptance criteria | Every PR | Reviewer other than the author's role |
| Traceability check (feature → requirement → test) | End of M1 and M3 | C – QA |
| Board and milestone review | Checkpoints Day 2, 5, 8 | A – PM |
| Evidence check before closing an Issue | Every Issue closure | Issue owner + QA |

## 4. Quality control activities (product)

| Activity | Deliverable | Method |
|---|---|---|
| Document review | Charter, requirements, WBS, schedule, risk register | Checklist below |
| Functional testing | Prototype (T07, T08) | Test cases in `test-cases.md` |
| Responsive check | Prototype | Browser at 360 px and 1280 px |
| Final verification | All Issues and milestones | `verification-report.md` (T11) |

### Document review checklist

- [ ] Matches the assignment requirement for this deliverable
- [ ] ID, version, date and role filled in
- [ ] Numbers are consistent with other documents (hours, dates, costs)
- [ ] Linked from its Issue

## 5. Definition of Done

An Issue moves to **Done** and is closed only when:

1. The deliverable file exists in `main` (merged Pull Request).
2. All acceptance criteria in the Issue are checked.
3. The work has been reviewed (PR review recorded).
4. *Actual Hours* is filled in on the Project Board.
5. The completion evidence link is posted in the Issue.

Issues are **never** closed only to raise the milestone percentage.

## 6. Defect management

Defects found in testing are recorded in `test-cases.md` (Actual result + Fail) and, if they need rework, as a GitHub Issue with the `testing` label linked to the failing test case. Severity: **High** blocks a mandatory feature, **Medium** degrades it, **Low** is cosmetic. High defects must be fixed before M3; Medium/Low may be documented as known issues.
