# 14: Hasil dan Pembahasan

**What to build:** An expectations-analysis section — an explicit labelling statement at the top,
a pre-registered-targets table, the expected-outcome analysis, and an honest-limits subsection.
It reports no measured data, because none exists before 18 Oct.

**Blocked by:** 13 (Metodologi).

**Status:** resolved

- [x] Top-of-section labelling statement: every result-shaped statement is an expectation.
- [x] Pre-registered targets table: one-way latency ≤ 200 ms; placement error within one grid cell.
- [x] Honest-limits subsection: tabletop proof of concept; no claim about real fuel-rod handling;
      no physical data before 18 Oct; fabrication = disqualification (guidebook p. 5 item 7).
- [x] Zero result-shaped statements presented as measured.
- [x] No unsourced claims.

## Answer (resolved 2026-10-17)

Hasil dan Pembahasan drafted at `.scratch/spc-full-paper/draft/14-hasil-dan-pembahasan-archonx.md`.

### Summary of what was built

1. **Top-of-section labelling statement & academic integrity commitment:**
   - Explicitly clarifies that all performance figures and metrics are pre-registered targets and engineering expectation analyses, not empirical measurements from physical hardware.
   - States clearly that physical assembly and quantitative testing are scheduled for 18 October 2026 for the Final stage (guidebook pp. 4, 13).
   - Directly cites the guidebook academic integrity clause (p. 5 item 7: fabrication = penalty or disqualification) to motivate why no empirical data is fabricated or claimed before real testing.

2. **Pre-registered targets table (Tabel 1):**
   - One-way latency: ≤ 200 ms over UDP Wi-Fi 2.4 GHz at 1 m and 3 m (rationalized by human teleoperation semi-real-time thresholds and indoor Wi-Fi delay models: Akl et al. 2006 [8], Pandey & Parasuraman 2021 [9]; evaluated via Eq 4).
   - Placement error: within 1 grid cell of target (Euclidean distance $e \le \text{grid cell size}$ for 30 mm × 30 mm × 30 mm test block; evaluated via Eq 5 and calibrated smartphone photo).
   - Success rate: project-defined 2-second hold criterion ($\ge$ 8 of 10 trials, 80% stable on target).
   - Comparative performance: Condition B (stick + fine mode) expected to achieve lower mean placement error ($\bar{x}_B < \bar{x}_A$) and lower standard deviation ($s_B < s_A$) compared to Condition A (coarse stick) by mitigating operator hunting.

3. **Expected-outcome analysis:**
   - Mechanism of fine-mode gain reduction $\alpha$ ($0 < \alpha < 1$): expands physical stick deflection for minute servo angle shifts, mitigating neuromuscular hunting and overshoot (supported by motion scaling literature: Richter et al. 2019 [4], Han & Yang 2022 [3]).
   - Release-to-hold natural locking: under rate control, stick recentering drops velocity command to zero ($v_{\text{arm}} = 0$), maintaining last joint angles without requiring bulky or costly mechanical clutches.
   - Wi-Fi 2.4 GHz transmission dynamics: log-distance path loss (Akl et al. 2006) and delay jitter/queuing (Pandey & Parasuraman 2021); why $\le$ 200 ms is critical to prevent move-and-wait operator behaviour.

4. **Honest-limits subsection:**
   - Tabletop proof of concept: explicitly limited to tabletop POC with lightweight foam blocks (30 mm × 30 mm × 30 mm). Absolutely no claim of real spent nuclear fuel handling, citing IAEA-TECDOC-1433 [1] and IAEA Radiation [2] regarding massive loads (hundreds of kg/tons), severe gamma radiation destroying commercial electronics/plastics, and hot-cell shielding requirements.
   - Open-loop limitations: TowerPro MG996R servos driven by PCA9685 operate strictly open-loop (no encoders, no torque/force sensors), meaning gear backlash, 3D printed structural compliance, and visual-only operator feedback constrain accuracy.
   - Zero physical data before 18 Oct: re-affirmed that zero measured physical numbers are reported in this draft.

### Verification

Programmatic verification executed via Python script:
- All 11 headers in `draft/14-hasil-dan-pembahasan-archonx.md` end with `-archonx`.
- Zero occurrences of prohibited interface terms (glove, IMU, MPU6050, web app / mobile app / Blynk as described primary interface) per `spec.md` Testing Decisions 7.
- All acceptance criteria elements verified present (top labelling, 18 Oct boundary, guidebook p. 5 item 7 disqualification rule, pre-registered targets table, tabletop POC limits, no real fuel rod claim, open-loop limits, project-defined 2s hold).
- Zero result-shaped claims presented as measured.
