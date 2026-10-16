---
Type: grilling
Status: resolved
Blocked by: 06
---

## Question

Specify the intervention the paper commits to, precisely enough that it could be implemented and
tested without further decisions:

- Which smoothing: low-pass/EMA, slew-rate limiting, or Kalman-style fusion of the MPU6050
  channels — and what filter constant/range?
- What "fine-positioning mode" means mechanically: gain reduction near the target, a clutch/re-hold
  behaviour, or a resolution multiplier? How is it entered and exited?
- Where it sits in the existing pipeline (ESP32 sender reading IMU -> Wi-Fi packet -> ESP32
  receiver -> PCA9685 PWM), and what it costs in latency.
- Failure behaviour: does smoothing ever fight the emergency-stop, the deadzone, or the
  clamp[theta_min, theta_max] safety limits already in the firmware?
- The physical intuition argument that goes in the paper: why jitter in the operator's hand maps to
  placement error, and why filtering it improves handling rather than just adding lag.

## Answer

**Committed intervention (settled with the user 14 Oct):** an **operator-triggered
fine-positioning mode** layered onto the base app teleoperation, implemented across the web-joystick
UI (ADR 0002) and receiver firmware.

Locked decisions:

1. **Trigger — explicit in-app fine-mode button** (user choice (a)); the operator decides when to
   switch. Adaptive/bubble variants recorded as design alternatives, not the committed design.
2. **Fine-mode behaviour (user accepted recommendation):**
   - **Gain reduction:** command-to-joint scale factor drops near the target (motion-scaling
     precedent: Richter 2019, Han & Yang 2022, Lee 2024 — see research/05-prior-art.md).
   - **Release-to-hold software latch:** releasing the joystick holds the last commanded position —
     the zero-cost software replacement for the literature's hardware clutch/rebinding. Framed in
     the paper as a design contribution of this work.
3. **Receiver untouched:** no encoders, no current sensing, PCA9685+servos stay open-loop; all
   positioning precision comes from the operator-side mode + firmware limits. Feedback-based
   autonomy stays in the future-work bucket (ADR 0001).
4. **Platform (per ADR 0002):** the UI is an ESP32-hosted web joystick (canvas joystick + fine
   button + gain control in the browser); Blynk Cloud is the documented fallback.

Evidence-basis rule (inherited from ticket 07): latency claims are pre-registered targets measured
in-team, never literature numbers; no Blynk-specific figure is cited.


**2026-10-15 (AMENDMENT, PS2 pivot):** Platform/UI clauses above (ESP32-hosted web joystick,
fine button in browser) are invalidated by the user's PS2-controller decision: fine mode moves to
the controller's **trigger** (independent toggle, Q9(i) approved). Gain-reduction +
release-to-hold semantics survive — under stick rate control, "release to hold" becomes natural:
stick centred = zero command velocity = arm holds. Receiver still untouched (open-loop). The
coordinated "stick forward = end-effector forward" rate layer is NEW scope beyond this ticket's
original answer and maps to the hybrid position/rate control prior art (research/05, Han & Yang
2022). Price evidence for the controller: verified first-page Tokopedia wireless PS2 = Rp85k+
(2026-10-15); wired "TW" clones are the class that can hit <Rp50k (price not verified live).
