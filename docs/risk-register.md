# Risk Register — CampusHelp

| | |
|---|---|
| **Document ID** | QA-02 (Issue T06) |
| **Version** | 1.0 |
| **Date** | 26 November 2026 |
| **Role** | Quality & Risk Coordinator (Student C) |

## 1. Scales

| Level | Probability | Impact |
|---|---|---|
| Low (1) | < 20 % | Delay < 0.5 day, no milestone affected |
| Medium (2) | 20–50 % | Delay 0.5–1 day or one deliverable reduced |
| High (3) | > 50 % | Milestone missed or a mandatory deliverable missing |

**Score = Probability × Impact** (1–9). Score ≥ 6 = red, 3–4 = amber, 1–2 = green.

## 2. Register

| ID | Risk (cause → effect) | Category | P | I | Score | Owner | Mitigation (before) | Contingency (if it happens) | Trigger | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R1 | Limited team capacity — a member is absent or overloaded → tasks on the critical path stop | Resource | 2 | 3 | **6** | A – PM | Balanced 15 h per role; critical-path tasks scheduled first; daily board review | Reassign critical tasks; use the 10 % reserve (4.5 h) | A task stays "In Progress" > 1 day without an update | Open |
| R2 | Requirements change (e.g. the Day 6 change request) → scope creep, schedule slips | Scope | 2 | 3 | **6** | A – PM | Formal change control: change-request Issue, impact analysis, decision record | Defer non-essential changes to a later phase | A new feature is requested after M1 | Open |
| R3 | Prototype defects found late → rework just before M3 | Quality | 2 | 3 | **6** | C – QA | Test cases written from requirements before prototyping; self-check during T07/T08 | Fix only defects that fail mandatory tests; document the rest | Any failed test case in T09 | Open |
| R4 | Design work (wireframes) is delayed → both prototype tasks start late | Schedule | 2 | 2 | 4 | B – BA | Low-fidelity wireframes only; prioritise the three core screens | Build the prototype directly from the requirements and update wireframes afterwards | T05 not "Done" by Day 4 | Open |
| R5 | GitHub access problem (permissions, Projects feature, account) → evidence cannot be recorded | Technical | 1 | 2 | 2 | A – PM | Access verified on Day 1; Projects scope enabled | Keep local copies; record evidence as soon as access returns | Push or board update fails | Closed (verified Day 1) |
| R6 | Missing evidence (screenshots, PR links) discovered at the end → marks lost | Quality | 2 | 2 | 4 | C – QA | Evidence link required before an Issue is closed; checklist in quality plan | Recreate evidence from Git history during T11 | Issue closed without "Completion evidence" | Open |
| R7 | Misunderstanding of the assignment requirements → wrong deliverable | Scope | 1 | 3 | 3 | B – BA | Requirements traced to the assignment checklist; questions asked in class | Rework the affected document in M4 | Lecturer feedback differs from plan | Open |

## 3. Heat map

| Impact → / Probability ↓ | Low (1) | Medium (2) | High (3) |
|---|---|---|---|
| **High (3)** | | | |
| **Medium (2)** | | R4, R6 | **R1, R2, R3** |
| **Low (1)** | | R5 | R7 |

## 4. Most serious risk

**R2 — Requirements change** is the most serious risk. R1, R2 and R3 have the same score (6), but R2 is the only one that is *certain* to be tested: a change request is planned for Day 6, at the point where the prototype is being built and only four working days remain. An uncontrolled change would hit the critical path (T07/T08 → T09 → T11 → T12) directly, increase cost and push the final deliverable past the deadline. It is also the risk the team controls least, because the request comes from the sponsor. The response is formal change control (`change-request.md`): no change is implemented without an impact analysis and a recorded decision.

## 5. Review log

| Date | Reviewer | Change |
|---|---|---|
| 26 Nov 2026 | PM | R5 closed — repository access, Issues and Projects verified |
| 26 Nov 2026 | QA | Register baselined (version 1.0) |
