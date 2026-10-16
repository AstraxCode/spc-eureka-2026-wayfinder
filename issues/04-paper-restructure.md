---
Type: grilling
Status: claimed
Blocked by: 01, 02, 03
---

## Question

Restructure the full paper around a solution rather than a comparison:

- New title (keeping the `-dingleberry` watermark convention) and how the Indonesian abstract reads
  once the contribution is an intervention, not a joystick-vs-glove finding.
- Section-by-section plan: which existing sections survive, which are rewritten, where the
  radiation/accuracy background is retained verbatim in substance, where the old comparison data
  goes (kept as motivation, demoted, or dropped).
- How the equations change: the existing clamp/scale mapping (eq. 2) versus the new filter
  equation, and which of the torque/latency/statistics equations (1, 3-6) remain.
- How the paper states its limits honestly — tabletop proof of concept, not a claim about real
  fuel-rod handling.
- What the expected results section promises, given results may not yet exist when it is written.


## Comments

**2026-10-15 (interview round 1-2, settled with user):**
- Title: deferred ("can go later") — still open within this ticket.
- Abstract reframe: ACCEPTED — contribution is the fine-positioning intervention; 2x2 protocol
  presented as planned validation; all results labelled expectations. Interface pitched as
  digital control on a phone (ESP32-hosted web app per ADR 0002; Blynk Cloud documented fallback).
- Section plan: ACCEPTED (Pendahuluan background verbatim; Dasar Teori rebuilt on motion
  scaling/hybrid position-rate control; Metodologi = web-joystick architecture + intervention +
  2x2; Kesimpulan/Saran restates contribution + limits).
- Hasil dan Pembahasan structure: ACCEPTED — expectations analysis + pre-registered targets table
  + explicit labelling statement at top + honest-limits subsection.
- Equations: ACCEPTED — eq (2) relabelled baseline coarse mapping; new fine-mode equation added;
  statistics eqs (4-6) retained.
- Glove/IMU AND analog joystick: REJECTED outright. Paper is digital-phone-control only
  (recorded as amendment in ticket 06 + ADR 0001).
- Glove in paper: ZERO mentions anywhere (user chose (a) over the future-work-sentence option,
  with the reviewer-question risk stated).
- Tujuan list: ACCEPTED replacement — (1) develop teleoperated arm controlled via digital
  smartphone app; (2) design fine-positioning mode; (3) test its effect on placement error,
  2-second hold success, one-way latency at 1 m/3 m per the 2x2 protocol.
- Expected results: option (b) — pre-registered numeric targets, clearly labelled, never
  presented as results. Latency target <= 200 ms (already in claim ledger as pre-registered);
  placement-error target = within one grid cell (defined by the grid markings, numeric value
  derived at draft time from the actual grid spacing, not invented).

**STILL OPEN in this ticket:** fine-mode mechanism semantics (round-2 Q9), title (deferred),
map updates + resolution once the interview closes.

**2026-10-16 (price + map update):** user supplies wired-PS2 price "around Rp40k-70k" as TEAM
ESTIMATE (verified live sweep 15 Oct: wireless >= Rp85k). The paper may use this figure only
labelled as team estimate, or with a captured listing link. Map updated; the stale Blynk
re-decision fog item cleared. REMAINING OPEN in this ticket: final title only.
