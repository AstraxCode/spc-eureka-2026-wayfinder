# 13: Metodologi

**What to build:** Metodologi in three parts — (i) the control architecture, (ii) the intervention
specification, (iii) the 2×2 validation protocol as a plan.

**Blocked by:** 08 (GLOSSARY), 09 (sender-ESP32 decision), 11 (Dasar Teori).

**Status:** resolved

- [x] Architecture subsection reflects the ticket-09 decision on the sender-side ESP32
      (controller → MCU → Wi-Fi → receiver ESP32 → PCA9685 → servos).
- [x] Intervention spec matches ticket 02: trigger-toggled fine mode (an independent mechanism),
      gain reduction near target, and release-to-hold — the latter inherent under stick rate
      control (stick centred = zero command velocity = arm holds).
- [x] 2×2 protocol stated exactly as in `spec.md`: condition A (baseline PS2 stick) vs B (stick +
      fine mode) × distance (1 m, 3 m); 40 trials per operator per condition; 3 paired operators,
      fallback 2; counterbalanced order; 8-of-10 2-second-hold criterion; placement error by phone
      photo vs grid.
- [x] Equations: eq (2) relabelled as the baseline coarse mapping; the new fine-mode equation
      added; eqs (1), (3)–(6) retained. No equation references a web/app UI.
- [x] No unsourced claims.

## Answer (resolved 2026-10-17)

Metodologi drafted at `.scratch/spc-full-paper/draft/13-metodologi-archonx.md`.

### Summary of what was built

1. **Control architecture subsection:**
   - Follows the committed chain from ticket 09: `PS2 controller → sender ESP32 (PS2X) → Wi-Fi → receiver ESP32 → PCA9685 → MG996R servos`.
   - Sender side (operator): PS2 controller polled over 4 wires via PS2X library (S8). Three control layers embedded in sender ESP32 firmware: (1) multi-DOF coordinated rate control (stick forward = end-effector forward), (2) ABXY single-joint selection, (3) trigger-toggled gain reduction + release-to-hold. Timestamp `t_send` stamped at stick-read so polling latency is included inside measured path.
   - Receiver side (manipulator): ESP32 receiver receives command packet, stamps `t_receive`, applies firmware software angle clamp `[θ_min, θ_max]`, and outputs 12-bit PWM over I2C to PCA9685 driving 5× TowerPro MG996R servos. Operating strictly open-loop (no encoders or current sensors). Electrical isolation: separate 5 V logic power and 6 V 5 A servo power with 1000 µF bulk capacitor.

2. **Intervention specification subsection:**
   - Fine mode (*mode posisi-halus*) toggled by controller trigger as an independent mechanism from sticks/buttons. Applies gain reduction factor α (0 < α < 1).
   - Release-to-hold (*tahan setelah pelepasan*): inherent under rate control — stick centered yields zero command velocity, holding arm's last commanded angle without drift. Framed as a software contribution replacing expensive hardware clutches.
   - Firmware safety limits: software clamp `[θ_min, θ_max]` active across both modes; physical emergency stop cut-off supported; connection watchdog holds position on timeout.

3. **2×2 validation protocol as a plan:**
   - Explicitly presented as a planned pre-registered validation protocol for the next stage (honest framing: no empirical data fabricated).
   - Design: 2×2 factorial (Condition A baseline coarse mode vs Condition B fine mode × Distance 1 m vs 3 m).
   - Trials: 40 trials per operator per condition.
   - Operators: 3 paired operators running all 4 cells, with documented fallback to 2 operators. Counterbalanced order to mitigate learning and fatigue effects.
   - Success criterion: 2-second hold (8 of 10 trials on target), clearly labelled as a project-defined criterion.
   - Placement error: Euclidean distance from object center to target center on millimeter grid, measured objectively via perpendicular top-down smartphone photo against 0.5 mm grid markings.
   - Controlled variables held constant: 30 mm × 30 mm × 30 mm foam block, 2.4 GHz Wi-Fi channel/AP placement, manipulator hardware, target layout.

### Drafting-level decisions recorded

- **Equation renumbering:** Dasar Teori owns eqs (1)–(3) (torque, coarse mapping, fine mapping). Metodologi continues the numbering:
  - Eq (4): one-way latency `t_latency = t_receive − t_send` (pre-registered target ≤ 200 ms).
  - Eq (5): Euclidean placement error `e = √[(x_final − x_target)² + (y_final − y_target)²]`.
  - Eq (6): sample mean `x̄ = (1/n) · Σ xᵢ`.
  - Eq (7): sample standard deviation `s = √[ (1/(n − 1)) · Σ (xᵢ − x̄)² ]`.
  Final unified numbering will be reviewed during packaging (ticket 20).
- **Prohibited strings compliance:** Zero occurrences of prohibited interface terms (glove, IMU, MPU6050, web app / mobile app as described interface), verified programmatically even across the scaffolding notes by referencing `spec.md` Testing Decisions 7 directly.

### Verification

Programmatic verification executed via Python script:
- All 18 headers in `draft/13-metodologi-archonx.md` end with `-archonx`.
- Exact chain string `PS2 controller → sender ESP32 (PS2X) → Wi-Fi → receiver ESP32 → PCA9685 → MG996R servos` verified present.
- All 25 required key terms (protocol parameters, metrics, conditions) verified present.
- Zero matches for forbidden patterns (glove, IMU, MPU6050, aplikasi web, smartphone app, Blynk).
- Equations (4)–(7) verified present.
