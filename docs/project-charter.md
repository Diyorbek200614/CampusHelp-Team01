# Project Charter — CampusHelp

| | |
|---|---|
| **Document ID** | PM-01 (Issue T01) |
| **Version** | 1.0 |
| **Date** | 26 November 2026 |
| **Prepared by** | Diyorjon Sobirov — Project Manager |
| **Course** | COSC 3500 IT Project Management |

## 1. Charter summary

| Charter component | Information |
|---|---|
| Project title | CampusHelp – University Student Service Request Portal |
| Business problem | Student service requests (IT support, classroom maintenance, library assistance, administrative services) arrive by e-mail and paper forms. They are hard to track, get lost, and students cannot see their progress. |
| Project objective | Plan and demonstrate a centralized, web-based request management portal in which students submit requests and follow them until they are resolved. |
| Project sponsor | University Administration (simulated) |
| Project manager | Diyorjon Sobirov (Student A) |
| Stakeholders | Students, IT support staff, administrators, maintenance staff, library staff |
| Project duration | 10 working days (26 Nov 2026 – 9 Dec 2026) |
| Project budget | 45 planned person-hours × 50,000 UZS = **2,250,000 UZS** (see `schedule-and-budget.md`) |
| In scope | Request submission, request categories and priorities, unique request ID tracking, administrator assignment, status updates, dashboard mockups and a clickable prototype |
| Out of scope | Real authentication, production server, database hosting, live SMS / e-mail services, integration with existing university systems |
| Success criteria | All four milestones completed and the prototype verified (see §4) |
| Constraints | Limited team capacity, 10 working days, no paid external services, GitHub Free only |

## 2. Business case

Today a request is an e-mail or a sheet of paper. Nobody owns it, it has no ID, and the student has to call or visit to find out what happened. The university therefore cannot measure how many requests it receives, how long they take, or which department is overloaded. A single portal gives every request an ID, an owner and a status, which makes the service measurable and transparent.

## 3. Proposed system features (high level)

1. Student request submission form.
2. Request categories (IT Support, Classroom Maintenance, Library, Administrative) and priority levels (Low, Medium, High).
3. Request tracking with a unique request ID (format `CH-YYYY-NNNN`).
4. Administrator assignment of a request to a staff member.
5. Request status updates (Submitted → Assigned → In Progress → Resolved / Closed).
6. A simple dashboard showing open, ongoing and completed requests.

## 4. Measurable success criteria

| # | Criterion | Measure | Target |
|---|---|---|---|
| SC1 | Feature coverage | Number of the six proposed features represented in requirements **and** in the prototype / mockups | 6 of 6 |
| SC2 | Milestone delivery | Milestones M1–M4 closed with all linked Issues closed and evidence attached | 4 of 4, each by its due date (±1 working day) |
| SC3 | Prototype quality | Mandatory test cases executed against the prototype | ≥ 6 test cases, 100 % executed, ≥ 90 % passed, all failures documented |
| SC4 | Effort control | Actual hours vs. planned 45 h | Variance ≤ 15 % (≤ 51.75 h) |
| SC5 | Traceability | Every closed Issue links to a document, prototype file or Pull Request | 12 of 12 |

## 5. Assumptions

- The university administration (simulated) is available to answer requirement questions during M1.
- Four request categories are sufficient for the pilot.
- Students use a modern web browser; mobile layout must work but no native app is required.
- The prototype may store data only in the browser (simulated back end).

## 6. Constraints

- **Time:** 10 working days, fixed final deadline.
- **People:** limited capacity; roles A, B and C are covered by the project team as described in `README.md`.
- **Cost:** no paid tools or services; GitHub Free.
- **Technology:** documentation in Markdown; prototype in plain HTML, CSS and JavaScript.

## 7. High-level risks

Detailed in `risk-register.md`. The most significant at charter stage: limited team capacity, requirement changes, and prototype defects discovered late.

## 8. Milestones

| Milestone | Due (Day) | Date | Key deliverables |
|---|---|---|---|
| M1 – Project Initiation | Day 2 | 27 Nov 2026 | Charter, requirements, stakeholders, initial WBS |
| M2 – Project Planning | Day 4 | 1 Dec 2026 | Schedule, resource estimates, risk register, mockups, quality plan |
| M3 – Project Execution | Day 7 | 4 Dec 2026 | Student request screen, admin dashboard, prototype demo, test cases |
| M4 – Monitoring and Closure | Day 10 | 9 Dec 2026 | Change request, verification report, final status, consolidated submission |

## 9. Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Sponsor (simulated) | University Administration | Approved | 26 Nov 2026 |
| Project Manager | Diyorjon Sobirov | Approved | 26 Nov 2026 |
