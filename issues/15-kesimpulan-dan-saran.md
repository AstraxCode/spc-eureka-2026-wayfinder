# 15: Kesimpulan dan Saran

**What to build:** Restate the contribution and the limits, and carry the camera-autonomy
future-work paragraph from ADR 0001.

**Blocked by:** 14 (Hasil dan Pembahasan).

**Status:** resolved

- [x] Restates the fine-positioning contribution and the limits consistently with ticket 14.
- [x] Contains exactly one future-work paragraph on camera-based autonomy (ADR 0001) — on record
      without becoming a second plan.
- [x] Introduces no new claims and no unsourced numbers.

## Answer

### Section draft created
The section is drafted and saved at `.scratch/spc-full-paper/draft/15-kesimpulan-dan-saran-archonx.md`
(6,621 characters, 4 markdown headers, all ending with the required internal watermark `-archonx`).

### Consistency and structure
1. **Restatement of fine-positioning contribution and limits (consistent with ticket 14):**
   - *Contribution:* Summarizes the operator-side fine-positioning intervention (*mode posisi-halus*)
     on a 5-DOF teleoperated robot arm via PS2 stick rate control and dual-microcontroller ESP32
     (UDP Wi-Fi 2.4 GHz). Highlights the gain reduction factor $\alpha$ ($0 < \alpha < 1$) toggled by the
     trigger button to expand physical stick dynamic range and mitigate neuromuscular hunting near the target.
   - *Release-to-hold:* Re-articulates the software latch replacing hardware clutches or brakes: centering
     the stick naturally commands zero angular velocity, holding the last joint angles on PCA9685 PWM registers.
   - *Tabletop proof-of-concept bounds:* Explicitly states that the system is a tabletop proof of concept
     using 30 mm synthetic foam blocks in a controlled laboratory, operating *strictly open-loop* (no encoders,
     no force/tactile sensors), and is categorically **not intended or claimed** for handling real spent nuclear
     fuel rods (citing IAEA-TECDOC-1433 and IAEA Radiation).
   - *Academic integrity and pre-registered status:* Reaffirms that all reported performance figures (latency
     $\le 200$ ms, placement error within 1 grid cell, 2-second hold with $\ge 8/10$ project-defined success rate)
     are pre-registered targets and theoretical design expectations, adhering to Eureka! ITB 2026 Guidebook p. 5
     item 7 prohibiting data fabrication prior to physical prototype testing on 18 October 2026.

2. **Camera-based autonomy future work (ADR 0001):**
   - Contains exactly one dedicated paragraph under *Saran dan Pengembangan Selanjutnya* documenting camera-based
     autonomous grasping as a long-term direction to reduce human operator cognitive load.
   - Accurately details why it was rejected for the full paper per ADR 0001 (hardware feasibility, budget constraints,
     avoiding unsourced/untested claims) and explicitly defines the three conditions required to unblock it
     (targeted literature review on low-cost vision manipulation, working demo before the next stage, and
     budget approval for vision compute) without turning into a competing second plan.

3. **No new claims, no unsourced numbers:**
   - Every metric (200 ms, 30 mm block, 2 s, 8/10 trials, 18 October 2026, 2×2 protocol parameters) is
     strictly carried from `spec.md`, `map.md`, `claim-ledger-archonx.md`, ticket 13, and ticket 14.

### Programmatic verification
- Header watermark check: 4 of 4 headers end with `-archonx` (100%).
- Prohibited strings check: 0 matches for `glove`, `sarung tangan`, `IMU`, `MPU6050`, `aplikasi web`,
  `smartphone app`, and `Blynk`.
- Camera autonomy paragraph check: exactly 1 focused future-work paragraph in Saran.
