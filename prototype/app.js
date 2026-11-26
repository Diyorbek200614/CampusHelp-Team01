/* CampusHelp prototype — simulated back end in browser localStorage.
   This is a demonstration only: no server, no authentication, no e-mail. */
const CH = (() => {
  const KEY = "campushelp.requests.v1";
  const CATEGORIES = ["IT Support", "Classroom Maintenance", "Library Assistance", "Administrative Services"];
  const PRIORITIES = ["Low", "Medium", "High"];
  const STATUSES = ["Submitted", "Assigned", "In Progress", "Resolved", "Closed"];
  const STAFF = {
    "IT Support": ["IT Support – Aziz K.", "IT Support – Malika R."],
    "Classroom Maintenance": ["Maintenance – Bekzod T."],
    "Library Assistance": ["Library – Nodira S."],
    "Administrative Services": ["Registrar – Kamola U."],
  };
  const OPEN = ["Submitted"];
  const ONGOING = ["Assigned", "In Progress"];
  const DONE = ["Resolved", "Closed"];

  const now = () => new Date().toISOString();

  function seed() {
    const y = new Date().getFullYear();
    const mk = (n, cat, pri, desc, status, staff) => {
      const hist = [{ at: "2026-11-24T09:10:00Z", text: "Submitted" }];
      if (staff) hist.push({ at: "2026-11-24T10:00:00Z", text: "Assigned to " + staff });
      if (status !== "Submitted" && status !== "Assigned") hist.push({ at: "2026-11-25T08:30:00Z", text: status });
      return { id: `CH-${y}-${String(n).padStart(4, "0")}`, studentId: "S" + (20260100 + n), name: "Sample student " + n,
        email: "", category: cat, priority: pri, location: "", description: desc, status, assignee: staff || "",
        createdAt: hist[0].at, history: hist };
    };
    return [
      mk(1, "IT Support", "High", "Wi-Fi does not work in the library reading room", "Resolved", "IT Support – Aziz K."),
      mk(2, "Classroom Maintenance", "Medium", "Broken chair in room A-105", "In Progress", "Maintenance – Bekzod T."),
      mk(3, "Library Assistance", "Low", "Request to extend book loan", "Assigned", "Library – Nodira S."),
      mk(4, "Administrative Services", "Medium", "Need an enrolment certificate", "Submitted", ""),
      mk(5, "IT Support", "Medium", "Cannot log in to the student portal", "Closed", "IT Support – Malika R."),
    ];
  }

  function load() {
    try {
      const raw = localStorage.getItem(KEY);
      if (raw) return JSON.parse(raw);
    } catch (e) { /* storage unavailable — fall through to seed */ }
    const data = seed();
    save(data);
    return data;
  }
  function save(list) {
    try { localStorage.setItem(KEY, JSON.stringify(list)); } catch (e) { /* ignore in private mode */ }
  }
  function nextId(list) {
    const y = new Date().getFullYear();
    const max = list.filter(r => r.id.startsWith(`CH-${y}-`))
      .reduce((m, r) => Math.max(m, parseInt(r.id.slice(-4), 10)), 0);
    return `CH-${y}-${String(max + 1).padStart(4, "0")}`;
  }

  /** Validates a submission. Returns {field: message} — empty object means valid. */
  function validate(d) {
    const e = {};
    if (!/^[A-Za-z]?\d{5,10}$/.test((d.studentId || "").trim())) e.studentId = "Enter a valid Student ID (5–10 digits, optional letter prefix).";
    if (!CATEGORIES.includes(d.category)) e.category = "Select a request category.";
    if (!PRIORITIES.includes(d.priority)) e.priority = "Select a priority level.";
    if ((d.description || "").trim().length < 10) e.description = "Describe the problem (at least 10 characters).";
    if (d.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(d.email.trim())) e.email = "Enter a valid e-mail address or leave it empty.";
    return e;
  }

  function submit(d) {
    const list = load();
    const r = {
      id: nextId(list), studentId: d.studentId.trim(), name: (d.name || "").trim(), email: (d.email || "").trim(),
      category: d.category, priority: d.priority, location: (d.location || "").trim(), description: d.description.trim(),
      status: "Submitted", assignee: "", createdAt: now(), history: [{ at: now(), text: "Submitted" }],
    };
    list.unshift(r);
    save(list);
    return r;
  }

  function find(id) {
    return load().find(r => r.id.toUpperCase() === (id || "").trim().toUpperCase()) || null;
  }

  function update(id, changes) {
    const list = load();
    const r = list.find(x => x.id === id);
    if (!r) return null;
    if (changes.assignee !== undefined && changes.assignee !== r.assignee) {
      r.assignee = changes.assignee;
      r.history.push({ at: now(), text: changes.assignee ? "Assigned to " + changes.assignee : "Assignment removed" });
      if (changes.assignee && r.status === "Submitted" && !changes.status) changes.status = "Assigned";
    }
    if (changes.status && changes.status !== r.status && STATUSES.includes(changes.status)) {
      r.status = changes.status;
      r.history.push({ at: now(), text: changes.status });
    }
    save(list);
    return r;
  }

  function counts(list) {
    return {
      open: list.filter(r => OPEN.includes(r.status)).length,
      ongoing: list.filter(r => ONGOING.includes(r.status)).length,
      done: list.filter(r => DONE.includes(r.status)).length,
      total: list.length,
    };
  }

  function reset() { save(seed()); }

  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const fmt = iso => new Date(iso).toLocaleString("en-GB", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
  const badge = s => `<span class="badge s-${s.replace(/\s/g, "")}">${esc(s)}</span>`;
  function toast(msg) {
    let t = document.querySelector(".toast");
    if (!t) { t = document.createElement("div"); t.className = "toast"; document.body.appendChild(t); }
    t.textContent = msg; t.style.display = "block";
    clearTimeout(t._h); t._h = setTimeout(() => (t.style.display = "none"), 2200);
  }

  return { CATEGORIES, PRIORITIES, STATUSES, STAFF, load, validate, submit, find, update, counts, reset, esc, fmt, badge, toast };
})();
