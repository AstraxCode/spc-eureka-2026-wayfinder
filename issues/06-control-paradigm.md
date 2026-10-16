---
Type: grilling
Status: resolved
Blocked by:
---

## Question

Manual vs autonomous control — which paradigm does the paper commit to? Explore BOTH paths inside
this single ticket as a criteria-based decision; do not fork the map into two parallel branches.

Criteria to weigh each path against:

1. **Background fit** — does "a human operator at distance from gamma radiation" still justify the
   design if the arm acts autonomously? The admin requires that background to survive.
2. **Hardware fit** — we own 2x ESP32, 5x MG996R + PCA9685 (no position feedback), 5x MPU6050 and a
   flex sensor. Those are operator-input devices, not object sensors: no camera, no grip-force
   sensor, no tactile array. Which path is buildable next stage without new parts?
3. **Evidence fit** — with zero trials before 18 Oct, which path can be argued credibly as design +
   labelled expected results?
4. **Delicate-handling fit** — which path can actually deliver "no crush, no drop, accurate
   placement" (settled definition) given servo-only grip control?
5. **Time** — what each path needs to reach a testable state inside the competition's stages.

Deliverable: ONE committed path for the paper, plus the rejected path written as an ADR
(domain-modeling: ADRs sparingly) stating why it lost and what would unblock it — that becomes the
paper's future-work paragraph, not a second plan.

Note: the metric decision in the map presumes teleoperation (latency retained). If autonomy wins,
Q4 must be re-opened.

## Comments

**2026-10-14 (user):** Adds two things. (1) The camera path stays on the table — the earlier
"no camera or object-force sensing" hardware assumption is RETRACTED (contradiction resolved:
user picked option (a)). (2) A third paradigm enters the comparison: **Blynk-app control** — a
custom-built joystick UI in the Blynk smartphone app drives the arm over Wi-Fi, and the
sender-side ESP32 is dropped to cut cost. So ticket 06 now weighs THREE paths, not two:
manual (existing glove/IMU/joystick), camera-based autonomy, Blynk-app control.

## Answer

**Committed paradigm: Blynk-app control.** A custom-built joystick UI in the Blynk smartphone
app drives the arm over Wi-Fi; the sender-side ESP32 is removed. Deployment includes a
**self-hosted local Blynk server** as the latency-sensitive mode alongside Blynk Cloud.

Criteria scoring (recap of the exchange):

| Criterion | Manual glove/IMU | Camera autonomy | **Blynk app** |
|---|---|---|---|
| Background fit | pass | pass | pass (human still remote) |
| Hardware fit | pass (owned) | fail (new camera + vision compute) | pass (phone + existing receiver) |
| Evidence fit | strong (motion-scaling literature) | none found for vision grasping | design-argument only, must be labelled as such |
| Delicate handling | achievable via fine mode | unproven | achievable via in-app fine mode |
| Time / cost | medium time | worst time | best cost (sender ESP32 cut); time: app + local server work |

**Decisions settled with the user (14 Oct):**
1. Camera-based autonomy: REJECTED — evidence fit, time, added hardware. Becomes the paper's
   future-work paragraph. ADR: `../adr/0001-reject-camera-based-autonomy.md`.
2. Manual glove/IMU path: NOT rejected — kept as a documented alternative for the Final-stage
   prototype (available if the committee asks about physical input hardware).
3. Latency stance: one-way latency stays a headline metric; the self-hosted local Blynk server is
   the deployment mode for latency-sensitive use, so the metric stays meaningful.
4. Ticket 02 scope confirmed: the intervention remains a motion-scaling / fine-positioning mode,
   implemented in the Blynk app + receiver firmware — the paper proposes a control solution, not
   just a cheaper input device.

**Follow-ups created:** ticket 07 (research: Blynk cloud vs local-server latency + offline
behaviour sourcing) — required before any Blynk latency claim enters the paper.

**2026-10-14 (AMENDMENT, post ticket-07 research):** the platform part of this answer is
superseded by ADR 0002 — primary interface is now an ESP32-hosted web joystick (no cloud), with
Blynk Cloud as documented fallback. Reason: current Blynk IoT has no public self-hosted server,
so the local-server latency mitigation chosen above is unavailable. The paradigm itself (app-based
teleoperation, sender ESP32 cut, human remote) is unchanged; metrics unchanged.

**2026-10-15 (AMENDMENT, during ticket 04):** Decision 2 above is RETRACTED by the user: the
manual glove/IMU path AND any analog physical joystick are REJECTED — the paper pitches digital
in-app control on a phone only. Glove no longer appears as a documented Final-stage alternative
or as a surveyed interface option in Dasar Teori; it may survive only in future-work/saran
framing if the user chooses. This amendment was made explicitly during the ticket-04 interview;
the paper's contribution statement is digital-control-only.


**2026-10-15 (AMENDMENT 2, during ticket 04 — PS2 controller pivot):** The same-day phone-only
digital ruling above is SUPERSEDED by a new user decision (user + team): the committed input
device is a **PS2 controller (joystick + ABXY + trigger), target price under Rp50.000**. The
paradigm remains human teleoperation; the phone/web-joystick UI of ADR 0002 is demoted. New
scheme: stick forward = end-effector forward (coordinated multi-DOF rate control), ABXY selects
a single joint then stick drives it (single-joint mode), trigger = fine-mode toggle
(independent, per user's approved Q9(i)). Consequences pending re-decision: ADR 0002 platform
line, ticket 02's web-joystick UI spec, and the one-way Wi-Fi latency metric definition (sender
ESP32 kept or removed). Pitch doc: ../../pitch-ps2-kontrol-archonx.md.

**2026-10-16 (AMENDMENT 3, ticket 09 resolved — sender-side ESP32 KEPT):** the re-decision named
"pending" in amendment 2 has landed. The **sender-side ESP32 is RETAINED**: it is the master MCU
that reads the PS2 controller (four-wire polled interface, PS2X library) and transmits commands
over Wi-Fi to the receiver ESP32. Reason: with the phone gone the operator side has no host at all
— a PS2 pad has no radio and only answers polls — so "no sender MCU" is reachable only by
reverting the input device to a screen, which amendment 2 demoted to documented fallback.

Consequences recorded here, in the original ticket (never a silent map overwrite):

1. **The "sender ESP32 removed" cost saving in this ticket's Answer is RETRACTED.** It was true of
   the phone interface only. What replaces it in the Feasibility argument: the sender ESP32 is a
   part the team **already owns** (the inventory carries 2x ESP32), so the interface change adds no
   MCU purchase, and the real saving is the glove hardware no longer needed (5x MPU6050 + flex
   sensor). Feasibility (15 percent of the rubric) now argues the 2-ESP32 design.
2. **The three control layers run on the sender ESP32's firmware**, not in an app: multi-DOF
   coordination kinematics (coarse), ABXY single-joint select, and the trigger-toggled gain
   reduction + release-to-hold of ticket 02's amendment.
3. **Chain committed:** PS2 controller → sender ESP32 (PS2X) → Wi-Fi → receiver ESP32 → PCA9685 → MG996R servos. Receiver unchanged, still open-loop.
4. **Latency:** `t_send` is stamped at the sender's stick-read, so the PS2X polling interval sits
   *inside* the measured path (identical in conditions A and B, so it does not bias the
   comparison). <= 200 ms stays a pre-registered in-team target, never a result. The polling rate
   has not been measured — no figure may be stated.
5. **Price:** the "<Rp50.000" line in amendment 2 is a *target*, not a verified price. The only
   live-verified figure is the wireless class at Rp85k+ (15 Oct sweep); the paper uses the
   wired-clone Rp40k-70k **team estimate** with that label, or no figure.

Platform line amended in ADR 0002 (amendment 2). Decision ticket: 09.
