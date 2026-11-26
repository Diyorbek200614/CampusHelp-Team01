# Change Request CR-01 — Automatic E-mail Acknowledgment

| | |
|---|---|
| **Document ID** | PM-03 (Issue T10) |
| **Change request ID** | CR-01 (GitHub Issue: see "Change-request Issue" below) |
| **Version** | 1.0 |
| **Date received** | 26 November 2026 (Day 6 event of the compressed schedule) |
| **Requested by** | University Administration (sponsor, simulated by the lecturer) |
| **Analysed by** | Project Manager (Student A) |

## 1. Requested change

> The university administration now wants students to receive an automatic email acknowledgment whenever a service request is submitted.

After a student submits a request, the system would send an e-mail to the student's address containing the request ID, category, priority and a link to track the request.

## 2. Is it inside the original scope?

**No.** The project charter (`project-charter.md`, *Out of scope*) explicitly excludes "live SMS / e-mail services", and requirement FR-12 in `requirements.md` is marked out of scope. The charter also has the constraint "no external service charges". The change therefore needs a formal decision; it cannot be added silently.

## 3. Effort and cost estimate

Rate: 50,000 UZS per person-hour.

| Option | Work | Effort | Cost (UZS) |
|---|---|---|---|
| **A. Simulated acknowledgment** (prototype only) | Update FR-12 (0.5 h); design an "e-mail preview" state in the confirmation screen (1 h); implement in prototype (0.75 h); add test case (0.5 h); update documents (0.25 h) | **3 h** (provisional estimate confirmed) | 150,000 |
| **B. Real e-mail sending** | Option A + choose and configure an e-mail service, sender domain/SPF, server-side sending code, failure handling, privacy review of student e-mail addresses, testing with real mailboxes | **≈ 9 h** (estimate revised upward) | ≈ 450,000 + recurring service cost |

The provisional three hours are realistic only for option A. Option B is about three times larger and needs a server, which the project does not have.

## 4. Affected tasks and milestones

| Item | Effect if approved |
|---|---|
| T02 Requirements | FR-12 moves into scope; e-mail field becomes mandatory |
| T05 Wireframes | W2 confirmation screen changes |
| T07 Student interface | New confirmation state and e-mail validation becomes mandatory |
| T09 Testing | New test case; TC-01 changes (e-mail now required) |
| T11, T12 | Verification and final report must include the change |
| M3 | Already completed → would be **re-opened** |
| M4 | Gains up to 3 h (A) or 9 h (B) of work |

## 5. Schedule, budget and risk impact

- **Schedule:** M3 is closed and the project is in its closure phase. Option A adds 3 h to the critical path (T07 → T09 → T11 → T12); option B cannot be completed before the final deadline at all.
- **Budget:** option A uses 150,000 UZS — 67 % of the 225,000 UZS contingency reserve; option B (≈ 450,000 UZS) exceeds the reserve by 225,000 UZS.
- **Risks:** raises R2 (requirements change) and R3 (late prototype defects) because a completed and tested screen would be changed at the end of the project. Option B also adds new risks: personal data (student e-mail addresses) sent to an external provider, and e-mail delivery failures.
- **Value:** the student already receives the request ID on screen (FR-05) and can track it (FR-06), so the core need — knowing that the request was received — is already met.

## 6. Recommendation and decision

**Decision: DEFER** to a later project phase (Phase 2, together with real authentication and hosting).

Justification:

1. It is outside the approved scope and conflicts with the charter constraint "no external service charges".
2. A real e-mail requires a production server and an e-mail provider — both out of scope for this project.
3. Implementing it now would re-open a completed and verified milestone (M3) during closure and consume most or all of the contingency reserve.
4. The business need is partly met already: the on-screen confirmation shows the request ID and tracking link.

Not rejected, because the request is reasonable and valuable once the system has a real back end.

## 7. Actions taken

| Action | Status |
|---|---|
| Change-request Issue created with label `change-request`, linked to T10 | Done |
| FR-12 in `requirements.md` marked "Deferred — CR-01" | Done |
| Baseline (scope, schedule, budget) | **Unchanged** — no revision needed because the change is deferred |
| Added to the Phase 2 backlog in `closure-report.md` | Done |

## 8. Decision record

| Role | Name | Decision | Date |
|---|---|---|---|
| Project Manager | Diyorjon Sobirov | Recommend: Defer | 26 Nov 2026 |
| Sponsor (simulated) | University Administration | Defer accepted | 26 Nov 2026 |
