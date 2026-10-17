# Map: SPC Eureka 2026 full paper repositioning

Status: closed
Tracker: local markdown — see docs/agents/issue-tracker.md (Wayfinding operations)

## Destination

A rewritten SPC full paper (team deadline 18 Oct 2026, official 23 Oct 2026) that presents a designed
solution to the accuracy/handling problem — committed control paradigm, specified intervention, and a
locked evaluation protocol — argued as design + explicitly-labelled expected results, since no
physical data can be collected before submission. Metrics retained: placement error, 2-second hold,
one-way latency.

## Notes

- Domain: SPC Eureka! ITB 2026 science project — teleoperated 5-DOF tabletop robot arm (2x ESP32,
  5x MPU6050, flex sensor, PCA9685, MG996R servos, direct Wi-Fi link).
- Skills every session should consult: `grilling`, `domain-modeling` (GLOSSARY/ADRs), `research`,
  `prototype`, `grounded-citations` (every external claim linkable), `paper-architecture`
  (`-archonx` watermark on title and section headers).
- Standing preferences: submission text Indonesian; blunt/direct style; never fabricate citations or
  data; keep facts, assumptions and recommendations visibly distinct.
- Admin permission (confirmed): any aspect of the paper may change EXCEPT the problem background —
  accuracy/handling when remotely handling radioactive material. That background stays intact.
- HARD CONSTRAINT (established 13 Oct): the prototype is locked behind the full-paper stage — zero
  trials are possible before 18 Oct. The paper cannot report new empirical results.
- Inventory findings (13 Oct, read-only sweep of both trees): NO trial data on disk anywhere (no
  CSV/XLSX/JSON/logs — only planned-protocol descriptions and cited literature values), confirming
  the labelled-expectations evidence basis. The full paper exists ONLY as the blank official
  template `Full paper/Format Full Paper.docx`, skeleton: PENDAHULUAN -> DASAR TEORI -> METODOLOGI ->
  HASIL DAN PEMBAHASAN -> KESIMPULAN -> DAFTAR PUSTAKA -> LAMPIRAN (Indonesian, IEEE-style example
  refs in the template). Control-intervention material on disk: one sentence on "penskalaan dan
  deadzone" + the clamp equation; ZERO mentions of smoothing, fine-positioning, calibration or
  feedback cues. Source-verified claims already curated in `claim-ledger-archonx.md`, which
  flags targets like "target <= 200 ms" as pre-registered targets, not results. The Obsidian vault
  tree is a byte-identical mirror; the SPC tree is the working copy.
- Dates: team internal 18 Oct, official 23 Oct 2026. Charted 13 Oct 2026.
- This effort drafts the paper itself once the map closes; the map only decides.
- SESSION DISCIPLINE: charting and working the map are SEPARATE authorizations. A "proceed" given
during charting authorizes charting only. No ticket gets claimed or resolved until the user opens
the working-the-map process explicitly.

## Decisions so far

Settled during charting, before any ticket existed (no ticket carries these):

- Destination is option (a): rewritten paper + locked experiment design. Not paper-only, not a full
  hardware/data build.
- Free surface: nothing beyond the accuracy/handling background is fixed — controllers, metrics,
  title, hardware all changeable in principle.
- Evidence basis: design + expected results, explicitly labelled as such — not simulation,
  not literature-only, pending whatever earlier data the inventory turns up.
- Metrics: keep all three — placement error, 2-second hold, one-way latency. This presumes
  teleoperation; revisit if ticket 06 commits to autonomy.
- Delicate handling, operationally: no crush, no drop, accurate placement.
- Control paradigm (ticket 06, resolved 14 Oct): **app-based teleoperation, sender ESP32 removed**
  *(superseded 15-16 Oct — see the PS2 amendment bullet and the ticket-09 decision below; the sender
  ESP32 is KEPT)*;
  camera-based autonomy rejected -> ADR 0001 (future-work paragraph); glove/IMU path kept as a
  documented Final-stage alternative. Platform AMENDED by ticket 07 + ADR 0002: primary interface
  is an **ESP32-hosted web joystick** (no cloud; current Blynk IoT has no self-hosted server), with
  Blynk Cloud as documented fallback.
- Intervention (ticket 02, resolved 14 Oct): operator-triggered **fine-positioning mode** — explicit
  in-app fine button, command-to-joint gain reduction near target, release-to-hold software latch
  (framed as this work's contribution, replacing the hardware clutch), receiver stays untouched
  (open-loop). Latency claims: pre-registered in-team targets only, never literature numbers.

- [Guidebook requirements](issues/01-guidebook-requirements.md): format/structure/deadlines extracted; no comparison-only penalty stated; design+expected-results basis supported; title-change rule not in guidebook (admin question).
- [Control paradigm](issues/06-control-paradigm.md): app-based teleoperation committed; camera
  autonomy rejected (ADR 0001); glove kept as documented alternative; metrics retained (still
  teleoperation). Platform amended -> ADR 0002.
- [Blynk sourcing](issues/07-blynk-sourcing.md): no public self-hosted Blynk server on current
  platform; no sourced local-server latency; rate limits 10 values/s flood / 20 req/s disconnect;
  three lower-tier Blynk-arm papers (unverified full texts); novelty supported.
- [Experiment protocol](issues/03-experiment-protocol.md): 2x2 (condition x distance 1m/3m);
  40 trials/operator/condition; 8/10 hold criterion; 3 paired operators (fallback 2);
  counterbalanced order; photo-vs-grid placement error; constants carried from abstract.
- [Intervention spec](issues/02-intervention-spec.md): fine mode = explicit button + gain reduction
  + release-to-hold latch; receiver untouched; platform = ESP32-hosted web joystick (ADR 0002).
- Admin ruling 14 Oct (via user): title edits ALLOWED; Pendahuluan + core problem LOCKED. Closes
  the title-change fog item; detail in ticket 01's answer section.
- [Prior art](issues/05-prior-art.md): motion scaling + hybrid position/rate control well supported; NO direct evidence smoothing alone improves placement accuracy (treat as hypothesis); 2-s hold is project-defined, not a standard metric.
- [GLOSSARY + domain wiring](issues/08-glossary-and-domain-wiring.md) (RESOLVED 16 Oct): root
  `GLOSSARY.md` created — 22 terms (the 12 required plus stick, fallback, operator, placement error,
  one-way latency, expected result, team estimate, receiver ESP32, sender-side ESP32, and the
  `-archonx` convention). Fine mode is defined as gain reduction and
  explicitly NOT smoothing/filtering/clutch; the sender-side-ESP32 entry records the retention
  question as OPEN (ticket 09) rather than settling it; `2-second hold` carries "project-defined"
  inside its definition. `AGENTS.md` + `docs/agents/domain.md` now point at the real ADR directory
  `.scratch/spc-full-paper/adr/`. This unblocks 11 → 13.
- [Paper restructure](issues/04-paper-restructure.md) (RESOLVED 16 Oct): abstract
  reframed to solution (fine-positioning contribution, results labelled expectations); section plan
  accepted (Pendahuluan background verbatim, Dasar Teori rebuilt on motion scaling/hybrid
  position-rate control, Metodologi = architecture + intervention + 2x2); Hasil dan Pembahasan =
  expectations analysis + pre-registered targets + honest-limits subsection; eq (2) relabelled
  baseline coarse mapping + new fine-mode equation added, statistics eqs (4-6) kept; Tujuan list
  replaced with the three-item solution-framed version; expected results = pre-registered numeric
  targets (latency <= 200 ms; placement error within one grid cell). Title left TEMPORARY by user
  decision (16 Oct) and carried to Issue #1 / drafting; user authorised proceeding past it.
- Control input AMENDED 15 Oct (tickets 06 + 02): glove/IMU and analog physical joystick
  REJECTED (zero mentions in paper), then same day superseded by the user+team decision: committed
  input device is a **PS2 controller** — stick = coordinated multi-DOF rate control (end-effector
  forward), ABXY = single-joint select, trigger = fine-mode toggle (independent mechanisms,
  Q9(i) approved). Phone/web-joystick UI demoted to documented fallback. Metrics + 2x2 protocol
  unchanged (condition A/B = baseline stick vs stick+fine mode).
- Price fact (16 Oct, user/team estimate — NOT a verified listing): wired PS2 clone "around
  Rp40k-70k". Verified live sweep 15 Oct found wireless units at Rp85k+ first-page Tokopedia.
  Paper must use the team-estimate label or a verified listing before submission. Pitch doc:
  `../../pitch-ps2-kontrol-archonx.md`.
- [Sender-side ESP32](issues/09-sender-esp32-decision.md) (RESOLVED 16 Oct): the sender-side ESP32
  is **KEPT** — the master MCU that reads the PS2 controller (four-wire polled interface, PS2X
  library) and transmits over Wi-Fi. Ticket 06's "sender ESP32 removed" cost saving is
  **RETRACTED** (ticket 06 amendment 3; ADR 0002 amendment 2). Feasibility now argues the 2-ESP32
  design: the sender ESP32 is an already-owned part (2x ESP32 inventory) and the glove hardware
  (5x MPU6050 + flex sensor) is no longer needed. Committed chain: PS2 controller → sender ESP32 (PS2X) → Wi-Fi → receiver ESP32 → PCA9685 → MG996R servos. `t_send` stamps at
  the sender's stick-read, so the unmeasured PS2X polling interval sits inside the latency path;
  <= 200 ms stays a pre-registered target.
- [Final title](issues/10-final-title.md) (RESOLVED 16 Oct): the title is decided and held in exactly
  one place, `.scratch/spc-full-paper/title.md` (`TITLE_INTERNAL` / `TITLE_SUBMISSION`) — Indonesian,
  solution-framed: it names the committed PS2-stick paradigm and the fine-positioning
  (mode posisi-halus) contribution, keeps the locked radioactive-material background clause, and
  carries none of the prohibited interface strings. The internal form keeps the `-archonx` watermark;
  the submitted cover title drops it (user decision). Closes the last open map item and GitHub Issue
  #1. Side effect: `GLOSSARY.md`'s Fine-mode Indonesian term aligned to *mode posisi-halus* (ticket 08
  amendment 1).
- [Dasar Teori](issues/11-dasar-teori.md) (RESOLVED 16 Oct): the section is drafted at
  `draft/11-dasar-teori-archonx.md` and rebuilt on the intervention's real prior art — motion scaling
  (Richter 2019; Yoon 2025), hybrid position/rate control (Han & Yang 2022; Lee 2024, abstract-level),
  and the filtering literature (Wang 2024) — with the honesty caveat stated outright: **no direct
  evidence that command smoothing alone improves placement accuracy**, so smoothing is a hypothesis and
  fine mode is not a filter. Ledger extended with S9–S13 / C14–C18 (the ticket-05 prior-art sources were
  not yet in the gate). This establishes the drafting convention `draft/NN-<slug>-archonx.md`, and the
  section owns eqs (1)–(3) (torque, coarse mapping, fine-mode gain reduction); the latency/statistics
  equations renumber at tickets 13/14–20. This unblocks 13.
- [Pendahuluan](issues/12-pendahuluan.md) (RESOLVED 16 Oct): drafted at
  `draft/12-pendahuluan-archonx.md`. Frozen-boundary check passes: the radiation/accuracy/handling
  background and the core problem are carried in substance from the Extended Abstract (admin ruling 14
  Oct), and the old comparison is demoted to motivation ("bukan lagi pertanyaan penelitiannya"). **User
  decision 16 Oct** resolved the C8 conflict: the unsourced mechanical-failure chain (C8 = NOT FOUND) and
  the element attribution (S2 supports only "ionizing radiation") are removed, and the dose/DNA claims are
  carried from the ledger (C1/C2, C3). No new ledger entry needed. Drafting-load split recorded in
  `drafting-loads-archonx.md`.
- [Metodologi](issues/13-metodologi.md) (RESOLVED 17 Oct): drafted at `draft/13-metodologi-archonx.md`.
  Divided into three parts: (i) control architecture reflecting the committed ticket-09 chain (`PS2 controller → sender ESP32 (PS2X) → Wi-Fi → receiver ESP32 → PCA9685 → MG996R servos`),
  with three firmware layers on sender ESP32 and open-loop operation on receiver ESP32 with power isolation;
  (ii) intervention specification detailing trigger-toggled fine mode (gain reduction factor α) and release-to-hold
  software latch as a cost-free alternative to literature hardware clutches; (iii) 2×2 validation protocol as a planned
  pre-registered experimental design (40 trials/condition, 3 paired operators with fallback to 2, counterbalanced order,
  project-defined 8-of-10 2-second-hold pass criterion, phone photo placement error measurement against millimeter grid).
  Equations renumbered cleanly: eq (4) latency, eq (5) Euclidean placement error, eq (6) sample mean, eq (7) sample standard deviation.
  Prohibited strings check passed cleanly. Unblocks 14.
- [Hasil dan Pembahasan](issues/14-hasil-dan-pembahasan.md) (RESOLVED 17 Oct): drafted at `draft/14-hasil-dan-pembahasan-archonx.md`.
  Divided into four parts: (i) explicit top-of-section labelling statement establishing that all metrics and analyses are pre-registered
  targets and engineering design expectations, directly citing the guidebook academic integrity rule (p. 5 item 7: fabrication = disqualification)
  and the 18 Oct prototype build milestone; (ii) pre-registered targets table (Tabel 1) specifying one-way latency ≤ 200 ms (UDP Wi-Fi 2.4 GHz,
  evaluated via Eq 4), Euclidean placement error within 1 grid cell (Eq 5), project-defined 2-second hold (8/10 trials), and expected
  variance reduction in Condition B vs Condition A (Eqs 6–7); (iii) expected-outcome analysis evaluating fine-mode gain reduction α
  against operator hunting (Richter et al. 2019, Han & Yang 2022), release-to-hold natural locking without mechanical clutches, and
  Wi-Fi propagation and latency jitter dynamics (Akl et al. 2006, Pandey & Parasuraman 2021); (iv) honest-limits subsection affirming
  tabletop proof-of-concept bounds using 30 mm foam blocks with explicit rejection of real nuclear fuel rod handling (IAEA-TECDOC-1433,
  IAEA Radiation), open-loop mechanical limitations (PCA9685, MG996R backlash/compliance), and zero physical measurements prior to 18 Oct.
  Prohibited strings check passed cleanly. Unblocks 15.
- [Kesimpulan dan Saran](issues/15-kesimpulan-dan-saran.md) (RESOLVED 17 Oct): drafted at `draft/15-kesimpulan-dan-saran-archonx.md`.
  Divided into two main sections: (i) Kesimpulan, restating the operator-side fine-positioning intervention (*mode posisi-halus*)
  via PS2 stick rate control and dual ESP32 architecture, elimination of mechanical clutches via *release-to-hold*, strict tabletop
  proof-of-concept boundaries (30 mm synthetic foam blocks vs real spent nuclear fuel rods per IAEA-TECDOC-1433 / IAEA Radiation),
  open-loop limitations, and reiteration of academic integrity adherence by presenting pre-registered targets (latency ≤ 200 ms,
  placement error within 1 grid cell, 2-second hold at ≥ 8/10 success rate) and theoretical expectations rather than fabricated
  data before 18 Oct 2026; (ii) Saran dan Pengembangan Selanjutnya, recommending full empirical execution of the 2×2 protocol
  during the Final stage, and containing exactly one dedicated future-work paragraph on camera-based autonomy (ADR 0001) recording
  its design-stage rejection and three unblocking prerequisites without becoming a competing second plan. Prohibited strings check
  passed cleanly (0 matches). Unblocks 16 (Abstrak).
- [Abstrak](issues/16-abstrak.md) (RESOLVED 17 Oct): drafted at `draft/16-abstrak-archonx.md`.
  Written in exactly one continuous paragraph of 224 words (within the 150–250 word requirement in guidebook/template)
  plus 5 alphabetical keywords (*faktor reduksi gain, lengan robot 5-DOF, mode posisi-halus, penanganan bahan radioaktif, teleoperasi stik PS2*).
  Reframed around the solution: states the primary contribution as the operator-side fine-positioning intervention (*mode posisi-halus*)
  via PS2 stick rate control and dual ESP32 architecture over Wi-Fi UDP, with trigger-activated gain reduction factor α (0 < α < 1)
  and inherent *release-to-hold* natural locking; presents the 2×2 factorial design as a planned pre-registered validation protocol;
  explicitly labels all result metrics (latency ≤ 200 ms, Euclidean error within 1 grid cell, 2s hold ≥ 80% success) as pre-registered
  targets and theoretical design expectations in strict compliance with academic integrity (guidebook p. 5 item 7); confirms tabletop
  open-loop bounds. Prohibited strings check passed cleanly (0 matches). Closes Load A sequence (12 → 13 → 14 → 15 → 16).

## Not yet specified

- Final title of the paper — **SETTLED 16 Oct 2026 (ticket 10).** The title is held in exactly one
  place, `.scratch/spc-full-paper/title.md` (`TITLE_INTERNAL` / `TITLE_SUBMISSION`): Indonesian,
  solution-framed, naming the committed PS2-stick paradigm and the fine-positioning contribution,
  keeping the locked radioactive-material background clause; internal form ends `-archonx`, and the
  submitted cover title drops that suffix (user decision). GitHub Issue #1 closed. Every other
  ticket-04 restructure decision is settled.
- Verified wired-PS2 listing price: team estimate is Rp40k-70k (16 Oct); a real listing link
  should be captured before the figure enters the paper.
- Physical prototype status and data boundary — **RESOLVED 17 Oct (ticket 14):** Hasil dan Pembahasan
  adopts the strict honest-limits convention: all results are explicitly labelled as pre-registered
  targets and theoretical expectations; physical testing is scheduled for 18 Oct for the Final stage;
  zero empirical measurements are fabricated, complying with guidebook p. 5 item 7.

## Out of scope

- Hardware modification before submission: no new sensors, no gripper redesign, no reprints. Whatever
  ticket 06 commits to must be buildable in the NEXT stage, not this one.
- Running any physical experiment as part of this submission (locked out by the constraint above).
- Anything outside this competition submission (publication, other contests, future productisation).
