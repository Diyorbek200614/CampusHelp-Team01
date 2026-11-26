# Project Closure Report — CampusHelp

| | |
|---|---|
| **Document ID** | PM-04 (Issue T12) |
| **Version** | 1.0 |
| **Date** | 26 November 2026 |
| **Prepared by** | Diyorjon Sobirov — Project Manager (roles A, B, C) |

## 1. Final status

**The project is closed.** All 12 mandatory tasks are complete, all four milestones are reached, the prototype is verified (8/8 test cases pass) and the only change request was formally decided (Deferred).

| Measure | Planned (original baseline) | Actual |
|---|---|---|
| Duration | 10 working days (26 Nov – 9 Dec 2026) | 1 working day (26 Nov 2026), after baseline revision 1 |
| Tasks | 12 | 12 completed |
| Milestones | 4 | 4 completed |
| Effort | 45 person-hours | ≈ 1.2 hours elapsed (recorded as Actual Hours on the board) |
| Cost at 50,000 UZS/h | 2,250,000 UZS (+ 225,000 reserve) | ≈ 60,000 UZS; reserve not used |
| Test cases | ≥ 6 | 8 executed, 8 passed (after one fix) |
| Defects | — | 1 found (Low), 1 fixed, 0 open |
| Change requests | — | 1 received, Deferred |
| Pull Requests | ≥ 3 | 16 merged |

## 2. Planned vs. actual completion by milestone

| Milestone | Original due | Revised due | Completed |
|---|---|---|---|
| M1 – Project Initiation | 27 Nov | 26 Nov | 26 Nov, 12:46 |
| M2 – Project Planning | 1 Dec | 26 Nov | 26 Nov, 12:48 |
| M3 – Project Execution | 4 Dec | 26 Nov | 26 Nov, 12:50 |
| M4 – Monitoring and Closure | 9 Dec | 26 Nov | 26 Nov (this report) |

## 3. Success criteria

See `verification-report.md` §4: SC1, SC2 (revised baseline), SC3 and SC5 met; SC4 (effort variance) not meaningful because the actual way of working differed fundamentally from the estimate's assumptions.

## 4. Major issues during the project

| Issue | Effect | Response |
|---|---|---|
| Late start — work began after the submission deadline | Original 10-day schedule impossible | Baseline revision 1: fast-tracking + crashing into one day; scope kept |
| One-person team instead of three | No independent peer review; all roles on one person | Lecturer's permission; roles kept separate in documents and PR reviews |
| Defect D-01 in the prototype | Duplicate history entry for students | Found by TC-07, fixed in PR #22, retested |
| Change request CR-01 during closure | Would re-open M3 and use the reserve | Formal impact analysis; Deferred to Phase 2 |
| Initial board screenshot not captured | Missing "initiation" evidence | Documented as a limitation; Roadmap and checkpoints show plan and progress |

## 5. Lessons learned

1. **Start on the day the work is assigned.** The biggest problem was not technical — it was the late start. One week of float was lost before day 1.
2. **Change control protects the deadline.** Writing an impact analysis before saying yes made the cost of the e-mail feature (≈ 9 h, a server, personal-data risk) visible; without it, the change would have looked like a small addition.
3. **Test before you close.** Testing found a real defect after both screens "looked finished". Closing T07/T08 only after review and running T09 immediately kept the fix cheap.
4. **Estimates depend on the way of working.** 45 hours assumed three people working manually; with AI assistance the documents and prototype took a fraction of that. Future estimates should state their assumptions and be re-estimated when the method changes.
5. **Evidence must be collected as you go.** Screenshots and links are easy to record at the moment and impossible to recreate later (initial board state).
6. **Dependencies drive the order of work.** Keeping Finish-to-Start links (T01 → T03, T05 → T07/T08 → T09) avoided rework even in a compressed schedule.

## 6. Unresolved work / Phase 2 backlog

| Item | Source | Priority |
|---|---|---|
| Automatic e-mail acknowledgment | CR-01 (Deferred) | High |
| Real back end and database | Charter — out of scope | High |
| Student and staff authentication | Charter — out of scope | High |
| Notifications to staff on assignment | Stakeholder analysis | Medium |
| Reporting (average resolution time per category) | Sponsor interest | Medium |

## 7. Individual reflection and accountability

I was responsible for all three roles: project manager, business analyst & designer, and quality & risk coordinator. I take responsibility for the late start, which was my decision and the reason the schedule had to be compressed. Doing every role myself showed me how much a project manager depends on the other roles: the schedule could only be built after the WBS, and the prototype could only be tested after the wireframes and requirements were fixed. The most useful practice for me was formal change control — saying "defer" with numbers is much easier than saying "no" without them. I used AI assistance, as permitted by the lecturer, to draft documents and the prototype; I reviewed the content, ran the tests and made the project decisions (schedule compression, deferral of CR-01). In my next project I will start on the day the work is assigned and capture evidence from the very first day.

## 8. Closure approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Project Manager | Diyorjon Sobirov | Project closed | 26 Nov 2026 |
| Sponsor (simulated) | University Administration | Deliverables accepted | 26 Nov 2026 |
