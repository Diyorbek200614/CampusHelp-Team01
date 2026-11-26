# Final Verification and Issue Review — CampusHelp

| | |
|---|---|
| **Document ID** | QA-05 (Issue T11) |
| **Version** | 1.0 |
| **Date** | 26 November 2026, 13:10 (Tashkent) |
| **Role** | Quality & Risk Coordinator (Student C) |
| **Depends on** | T09 Testing, T10 Change request |
| **Method** | Every Issue and Pull Request checked through the GitHub API and on GitHub against the Definition of Done in `quality-plan.md` |

## 1. Issue review

| Issue | Task | State | Acceptance criteria ticked | Evidence link in Issue | Closed by PR | Progress updates |
|---|---|---|---|---|---|---|
| #1 | T01 Project charter | Closed | 4/4 | Yes | #13 | 3 |
| #2 | T02 Requirements | Closed | 4/4 | Yes | #14 | 3 |
| #3 | T03 Scope & WBS | Closed | 4/4 | Yes | #15 | 3 |
| #4 | T04 Schedule & budget | Closed | 4/4 | Yes | #16 (+ #23 baseline revision) | 5 |
| #5 | T05 Wireframes | Closed | 4/4 | Yes | #17 | 3 |
| #6 | T06 Risk register & quality plan | Closed | 4/4 | Yes | #18 | 3 |
| #7 | T07 Student interface | Closed | 4/4 | Yes | #19 | 3 |
| #8 | T08 Admin dashboard | Closed | 4/4 | Yes | #20 | 3 |
| #9 | T09 Test cases | Closed | 4/4 | Yes | #22 (+ #21 first run) | 4 |
| #10 | T10 Change request | Closed | 4/4 | Yes | #25 | 3 |
| #11 | T11 Final verification | This document | — | — | — | — |
| #12 | T12 Final report | Open — next task | — | — | — | — |
| #24 | CR-01 E-mail acknowledgment | Closed (Deferred) | n/a | Decision comment → PR #25 | #25 | 2 |
| #26 | Status reports | Open until closure | n/a | 3 checkpoint comments, PR #27 | — | 3 |

Result: all ten completed mandatory Issues meet the Definition of Done. No Issue was closed without a merged deliverable.

## 2. Milestone review

| Milestone | Issues | Result |
|---|---|---|
| M1 – Project Initiation | T01–T03 closed | Complete |
| M2 – Project Planning | T04–T06 closed | Complete |
| M3 – Project Execution | T07–T09 closed | Complete |
| M4 – Monitoring and Closure | T10 closed; T11, T12 closing now | Completes with T12 |

All four milestones have descriptions and calendar due dates (revised to 26 Nov 2026 by baseline revision 1; original dates kept in `schedule-and-budget.md` §8).

## 3. Deliverable check

| Deliverable | File | Present in `main` |
|---|---|---|
| Charter | `docs/project-charter.md` | ✔ |
| Requirements & stakeholders | `docs/requirements.md` | ✔ |
| WBS | `docs/wbs.md` | ✔ |
| Schedule, dependencies, budget | `docs/schedule-and-budget.md` | ✔ |
| Wireframes | `docs/wireframes.md` | ✔ |
| Risk register | `docs/risk-register.md` | ✔ |
| Quality plan | `docs/quality-plan.md` | ✔ |
| Student request screen + tracking | `prototype/index.html`, `prototype/track.html` | ✔ |
| Admin dashboard | `prototype/admin.html` | ✔ |
| Test cases (8, all passed after fix) | `docs/test-cases.md` | ✔ |
| Change request & decision | `docs/change-request.md` | ✔ |
| Checkpoints 1–3 | `docs/monitoring/` | ✔ |

## 4. Success criteria (charter §4)

| # | Criterion | Target | Result |
|---|---|---|---|
| SC1 | Feature coverage | 6 of 6 | **Met** — all six features in requirements, wireframes and prototype |
| SC2 | Milestone delivery | 4 of 4 by due date | **Met** against the revised baseline; original 10-day plan replaced by the compressed baseline |
| SC3 | Prototype quality | ≥ 6 tests, 100 % executed, ≥ 90 % pass | **Met** — 8 tests, 100 % executed, 100 % pass after fix |
| SC4 | Effort control | variance ≤ 15 % of 45 h | **Not meaningful** — actual effort far below estimate (see closure report) |
| SC5 | Traceability | 12 of 12 Issues with evidence | **Met** for T01–T10; T11–T12 complete with this PR and the final report |

## 5. Assignment checklist

| Item | Status |
|---|---|
| Exactly three team members have access | **Deviation** — individual submission permitted by the lecturer; one member covers roles A, B, C |
| Project charter and WBS completed | ✔ |
| Four GitHub milestones created with due dates | ✔ |
| Twelve mandatory Issues created and assigned | ✔ |
| Priority, hours and date fields populated | ✔ (Actual Hours filled at closure) |
| Board, Table and Roadmap views available | ✔ (views created on the Project Board) |
| Three Pull Requests and peer-review evidence | ✔ 13 PRs; review comments per PR — reviews are role-based self-reviews because there is no second member |
| Risk register and change request completed | ✔ |
| Three progress checkpoints documented | ✔ |
| Testing and project closure completed | ✔ with T12 |
| Final PDF and GitHub links ready | with T12 |

## 6. Outstanding work and known limitations

1. **Team-size deviation:** no real peer review by another person was possible; each PR has a review comment against the acceptance criteria written from the reviewing role.
2. **Board history:** the board at "initiation" was not captured as a screenshot before work began; the Roadmap view and the checkpoint reports show the planned and intermediate states instead.
3. **Compressed schedule:** the 10-day plan was replaced by a one-day baseline (baseline revision 1); checkpoints were held at equivalent points of the day.
4. **Deferred scope:** CR-01 (automatic e-mail) is in the Phase 2 backlog.
5. **Prototype limitations:** no real back end, authentication or e-mail (documented in `test-cases.md`).

## 7. Conclusion

The project is ready for closure. All completed work is merged and traceable; the deviations above are documented and do not block closure.
