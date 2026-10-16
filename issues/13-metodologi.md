# 13: Metodologi

**What to build:** Metodologi in three parts — (i) the control architecture, (ii) the intervention
specification, (iii) the 2×2 validation protocol as a plan.

**Blocked by:** 08 (GLOSSARY), 09 (sender-ESP32 decision), 11 (Dasar Teori).

**Status:** ready-for-agent

- [ ] Architecture subsection reflects the ticket-09 decision on the sender-side ESP32
      (controller → MCU → Wi-Fi → receiver ESP32 → PCA9685 → servos).
- [ ] Intervention spec matches ticket 02: trigger-toggled fine mode (an independent mechanism),
      gain reduction near target, and release-to-hold — the latter inherent under stick rate
      control (stick centred = zero command velocity = arm holds).
- [ ] 2×2 protocol stated exactly as in `spec.md`: condition A (baseline PS2 stick) vs B (stick +
      fine mode) × distance (1 m, 3 m); 40 trials per operator per condition; 3 paired operators,
      fallback 2; counterbalanced order; 8-of-10 2-second-hold criterion; placement error by phone
      photo vs grid.
- [ ] Equations: eq (2) relabelled as the baseline coarse mapping; the new fine-mode equation
      added; eqs (1), (3)–(6) retained. No equation references a web/app UI.
- [ ] No unsourced claims.
