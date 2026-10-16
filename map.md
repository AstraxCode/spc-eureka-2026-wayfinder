# Map: SPC Eureka 2026 full paper repositioning

Status: open
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
  (`-dingleberry` watermark on title and section headers).
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
  feedback cues. Source-verified claims already curated in `claim-ledger-dingleberry.md`, which
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
- Control paradigm (ticket 06, resolved 14 Oct): **app-based teleoperation, sender ESP32 removed**;
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
  `-dingleberry` convention). Fine mode is defined as gain reduction and
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
  `../../pitch-ps2-kontrol-dingleberry.md`.

## Not yet specified

- Final title of the paper — STILL NOT CHOSEN. User confirmed 16 Oct that the working title stays
  TEMPORARY and authorised the effort to proceed past it. Live on GitHub Issue #1; must be
  finalised before submission. Every other ticket-04 restructure decision is settled (see
  Decisions so far).
- Verified wired-PS2 listing price: team estimate is Rp40k-70k (16 Oct); a real listing link
  should be captured before the figure enters the paper.


- Whether the arm physically exists as a BUILT prototype: no digital evidence in either tree (no
  photos, no firmware, no STL). The extended abstract states build steps in past tense — either
  build evidence lives outside these dirs (phone photos etc.) or the wording overstates. Only the
  team can settle this; HASIL DAN PEMBAHASAN wording depends on it.
- Sender-side ESP32 kept or removed under the PS2 scheme (ticket 06 amendment 2). A PS2
  controller needs a master MCU to read it, so ticket 06's "sender ESP32 removed" cost claim
  cannot stand as written; re-decide before the Metodologi architecture and Feasibility argument
  are written.

## Out of scope

- Hardware modification before submission: no new sensors, no gripper redesign, no reprints. Whatever
  ticket 06 commits to must be buildable in the NEXT stage, not this one.
- Running any physical experiment as part of this submission (locked out by the constraint above).
- Anything outside this competition submission (publication, other contests, future productisation).
