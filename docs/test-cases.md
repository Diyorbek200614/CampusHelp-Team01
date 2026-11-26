# Test Cases and Results — CampusHelp Prototype

| | |
|---|---|
| **Document ID** | QA-04 (Issue T09) |
| **Version** | 1.2 |
| **Date** | 26 November 2026 |
| **Role** | Quality & Risk Coordinator (Student C) |
| **Depends on** | T07 Student interface, T08 Administrator dashboard |
| **Test object** | `prototype/` (HTML/CSS/JS, served locally at `http://localhost:5610`) |
| **Environment** | Chromium-based browser, Windows 11, desktop width; mobile layout checked at 375 px |

## What is real and what is simulated

| Function | Implementation in the prototype |
|---|---|
| Form, validation, confirmation, request ID, tracking, assignment, status change, dashboard counts and filters | **Implemented** in JavaScript |
| Data storage | **Simulated** — browser `localStorage`; 5 sample requests are loaded on first use |
| Users / login | **Not implemented** — the admin page is open (out of scope) |
| E-mail acknowledgment | **Not implemented** — see `change-request.md` |

## Test cases

| ID | Requirement | Steps | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC-01 | FR-01, FR-02 Required fields | 1. Open *Submit request*. 2. Leave all fields empty. 3. Click **Submit request**. | Form is not submitted; error text appears under Student ID, Category, Priority and Description; no new request is stored. | Errors shown for exactly those 4 fields ("Enter a valid Student ID…", "Select a request category.", "Select a priority level.", "Describe the problem…"); confirmation hidden; stored requests stayed at 5. | **Pass** |
| TC-02 | FR-03 Category selection | 1. Open the Category list. | Exactly 4 categories: IT Support, Classroom Maintenance, Library Assistance, Administrative Services, plus the "Select a category" placeholder. | The 4 categories and the placeholder are listed. | **Pass** |
| TC-03 | FR-04 Priority selection | 1. Check the priority options. 2. Fill all other required fields, leave priority empty, submit. | Options Low, Medium, High; submitting without priority shows only the priority error. | Options Low, Medium, High. Only `priority` was marked invalid. | **Pass** |
| TC-04 | FR-05 Confirmation after submission | 1. Enter Student ID 20261234, category IT Support, priority High, location Room B-204, description "Projector in B-204 does not turn on". 2. Submit. | Confirmation screen with a new unique ID `CH-2026-NNNN`, category, priority and status *Submitted*. | Confirmation shown: **CH-2026-0006**, IT Support, High, *Submitted*; stored requests 5 → 6. | **Pass** |
| TC-05 | FR-06, FR-11 Status visibility | 1. Click **Track this request** (or enter CH-2026-0006 on *Track*). 2. Enter a non-existent ID CH-2026-9999. | Request details, current status and dated history are shown; for an unknown ID a clear "not found" message. | Details, status and history displayed; unknown ID → "No request found with ID CH-2026-9999. Check the ID and try again." | **Pass** |
| TC-06 | FR-09 Dashboard information | 1. Open *Admin*. 2. Compare tiles with the data (5 samples + CH-2026-0006). | Open = Submitted, Ongoing = Assigned + In Progress, Completed = Resolved + Closed, Total = all. | Open 2, Ongoing 2, Completed 2, Total 6 — matches the data (0004, 0006 / 0002, 0003 / 0001, 0005). 6 rows listed. | **Pass** |
| TC-07 | FR-07, FR-08 Assignment and status update | 1. On *Admin*, assign CH-2026-0006 to "IT Support – Aziz K.". 2. Change its status to *In Progress*. 3. Open it on *Track*. | Status becomes *Assigned* after assignment, then *In Progress*; tiles update (Open 1, Ongoing 3); history shows one entry per change. | Run 1: status and tiles correct, **but the history contained a duplicate entry** ("Assigned to IT Support – Aziz K." **and** "Assigned"). Defect D-01 raised. Run 2 (after fix, request CH-2026-0004 assigned to "Registrar – Kamola U." then set to *In Progress*): status Assigned → In Progress; tiles Open 1→0, Ongoing 3→4; history "Submitted", "Assigned to Registrar – Kamola U.", "In Progress" — no duplicate. | Run 1 **Fail** → Run 2 **Pass** |
| TC-08 | FR-10 Dashboard filters | 1. Filter Category = IT Support. 2. Add Priority = High. 3. Clear both, filter Status = Submitted. | Only matching rows are listed for each filter combination. | IT Support → 0006, 0001, 0005. + High → 0006, 0001. Submitted → 0004. | **Pass** |

## Defects

| ID | Found in | Severity | Description | Fix | Retest |
|---|---|---|---|---|---|
| D-01 | TC-07 run 1 | Low | Assigning an unassigned request wrote two history entries ("Assigned to …" and "Assigned"), so the student saw the same event twice. | `CH.update()` sets the status to *Assigned* without a second history entry when the change is caused by the assignment itself. | TC-07 run 2 — **Pass**, defect closed |

## Summary

| Metric | Value |
|---|---|
| Test cases | 8 (6 mandatory areas covered) |
| Executed | 8 of 8 (100 %) |
| Passed on first run | 7 of 8 (87.5 %) |
| Defects found | 1 (Low) |
| Passed after fix | 8 of 8 (100 %) |
| Open defects | 0 |
