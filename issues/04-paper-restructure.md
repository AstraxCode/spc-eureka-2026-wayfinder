---
Type: grilling
Status: resolved
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

**2026-10-15 (AMENDMENT, PS2-controller pivot — written into this ticket 2026-10-16):**
The PS2-controller decision (recorded 15 Oct in tickets 06 and 02, and in the map's
Decisions-so-far) invalidates the phone/web-joystick framing that the round-1/2 answers below
were given under. Recording the consequences here so the ticket is not internally
contradictory:

- **Interface, everywhere:** the committed input device is a **PS2 controller** (analog stick +
  ABXY + trigger). No "aplikasi web" / "smartphone app" wording survives in the paper. The
  ESP32-hosted web joystick (ADR 0002) is demoted to a documented fallback.
- **Tujuan list — item 1 revised only:** (1) develop a teleoperated arm controlled via a **PS2
  controller**; (2) design a fine-positioning mode; (3) test its effect on placement error,
  2-second hold success, and one-way latency at 1 m / 3 m per the 2x2 protocol. Items 2 and 3
  stand as accepted.
- **Fine-mode mechanism (Q9(i), approved):** the controller's **trigger** is the fine-mode
  toggle — an independent mechanism from the stick and ABXY. Gain reduction + release-to-hold
  survive unchanged under stick rate control (stick centred = zero command velocity = arm
  holds).
- **Section plan:** Metodologi's architecture description becomes PS2 -> ESP32 -> Wi-Fi ->
  receiver ESP32 -> PCA9685 -> servos. Pendahuluan background still retained in substance; Dasar
  Teori still motion scaling / hybrid position-rate control; 2x2 still the validation protocol.
- **Equations:** eq (2) stays the relabelled baseline coarse mapping; the new fine-mode equation
  is unchanged (gain reduction is device-agnostic). No equation depends on the web UI.
- **Condition A/B naming:** A = baseline PS2 stick control; B = PS2 stick + fine mode.
- **CARRIED, NOT SETTLED HERE:** whether the sender-side ESP32 is kept under the PS2 scheme — see
  ticket 06 amendment 2. A PS2 controller needs a master MCU to read it (PS2X library), so
  ticket 06's "sender ESP32 removed" cost claim cannot stand as written.

## Answer

**Resolved 2026-10-16.** The restructure is fully specified. The one item this ticket cannot
close on its own is the final **title**, which the user explicitly left **TEMPORARY** on 16 Oct
while authorising the effort to proceed past it (tracked as GitHub Issue #1; must be finalised
before submission).

Settled across interview rounds 1-2 (15 Oct) plus the 15 Oct PS2 amendment above:

1. **Contribution / abstract:** the fine-positioning intervention is the contribution; the 2x2
   protocol is presented as planned validation; every result is labelled an expectation.
2. **Title:** TEMPORARY, not committed. The pre-PS2 draft ("...Berbasis Aplikasi Web...") is
   void. The final title must not contain "aplikasi web" or "smartphone app".
3. **Section plan:** Pendahuluan = accuracy/handling background retained in substance (locked by
   the 14 Oct admin ruling); Dasar Teori rebuilt on motion scaling + hybrid position/rate
   control; Metodologi = PS2 architecture + intervention + 2x2; Hasil dan Pembahasan =
   expectations analysis + pre-registered targets table + explicit labelling statement +
   honest-limits subsection; Kesimpulan/Saran restates contribution + limits.
4. **Old comparison data:** demoted to motivation inside Pendahuluan / Dasar Teori, never a
   results section; the baseline-vs-fine-mode 2x2 replaces it.
5. **Equations:** eq (2) relabelled baseline coarse mapping; new fine-mode equation added;
   torque/latency/statistics eqs (1, 3-6) retained, statistics eqs (4-6) unchanged.
6. **Honest limits:** tabletop proof of concept; no claim about real fuel-rod handling; no
   physical data before 18 Oct; fabrication = disqualification (guidebook p. 5 item 7).
7. **Expected results:** pre-registered numeric targets only — one-way latency <= 200 ms
   (already in the claim ledger as a pre-registered target) and placement error within one grid
   cell (numeric value derived at draft time from the actual grid spacing, never invented).
8. **Interface:** PS2 controller committed; ESP32-hosted web joystick (ADR 0002) demoted to
   documented fallback; glove/IMU and analog physical joystick — zero mentions anywhere.

**Carried forward (not blockers for this ticket):**

- Final title -> GitHub Issue #1 and the drafting stage.
- Sender-side ESP32 kept-or-removed -> ticket 06 amendment 2; must be settled before the
  Metodologi architecture and the Feasibility argument are written.
- Verified wired-PS2 listing price -> the team estimate Rp40k-70k stands only with its
  team-estimate label until a real listing link is captured.
