# 19: Lampiran

**What to build:** Appendices for the circuit/wiring and component material.

**Blocked by:** None (can start immediately).

**Status:** resolved

- [x] Wiring/circuit schematic (`skema-rangkaian-teleoperasi-archonx`) and component table
      (`tabel-komponen-archonx`) included and legible.
- [x] Consistent with the Metodologi architecture once ticket 13 lands.
- [x] The PS2 controller price carries its team-estimate label (Rp40k–70k); no unverified figure
      stated as fact.
- [x] No "aplikasi web" / "smartphone app" wording.

## Answer

**Resolved 2026-10-17 (ArchonX).** Draft: `.scratch/spc-full-paper/draft/19-lampiran-archonx.md`.

### Deliverables and Template Alignment

Formatted strictly per the competition guidelines (`Full paper/Format Full Paper.docx` lines 127–168):
1. **Lampiran 1 (Pembagian Tugas):** Detailed task allocation across all three team members (Anargya Arkan Dhafy Hamdani as Ketua Tim, Muhamad Naufal Firdaus as Anggota 1, Fakhri Ahmad Kendri as Anggota 2).
2. **Lampiran 2 (Rincian Anggaran Biaya):** Realistic component budget formatted per the template table structure. The PS2 controller price explicitly carries the mandatory label **`(Perkiraan tim: Rp40.000–Rp70.000)`** with unit estimate Rp55.000; total budget Rp725.000.
3. **Lampiran 3 (Spesifikasi Komponen / `tabel-komponen-archonx`):** 3-column table (`Komponen | Spesifikasi | Fungsi`) aligned with the committed PS2 teleoperation architecture (5-DOF arm, MG996R servos, PCA9685 driver, dual ESP32 DevKit, isolated power rails, and bulk decoupling capacitor).
4. **Lampiran 4 (Skema Rangkaian Kelistrikan / `skema-rangkaian-teleoperasi-archonx`):** Full ASCII system block diagram and complete pinout wiring tables for:
   - PS2 controller → ESP32 Sender via 4-wire SPI-like interface (`DATA` GPIO 19, `CMD` GPIO 23, `ATT` GPIO 5, `CLK` GPIO 18).
   - ESP32 Receiver → PCA9685 via I2C (`SDA` GPIO 21, `SCL` GPIO 22).
   - PCA9685 → 5× MG996R servo channels (CH0..CH4) with software angle clamps.
   - Dual-rail power architecture (6V 5A servo rail, 5V logic rail, common ground, 1000 µF bulk capacitor).
5. **Lampiran 5 (Algoritma Kendali):** Documented pseudocode implementation for the fine-positioning mode gain scaling ($G = 0,25$) and release-to-hold neutral latching mechanism.

### Consistency with Metodologi Architecture

Aligned with the committed chain locked in tickets 06, 09, and 10:
`PS2 controller → sender ESP32 (PS2X) → Wi-Fi → receiver ESP32 → PCA9685 → MG996R servos`.

### Verification Run (Executed)

Programmatic validation via Python:
- Prohibited wording audit: `aplikasi web`: 0, `smartphone app`: 0, `sarung tangan sensor`: 0, `glove`: 0.
- PS2 controller estimate label: verified present (`perkiraan tim: Rp40.000–Rp70.000`).
- Architecture components verified present: PS2, ESP32, PCA9685, MG996R, Wi-Fi.
- All 11 markdown headers end with the `-archonx` watermark.

### Staging Note for Load A (archonx01)
Shared-file discipline respected: no direct edits to `map.md`, `claim-ledger-archonx.md`, or `WORKFLOW-paper-development.md`. Ticket 19 resolution and Lampiran tables/diagrams are staged here for Load A to reference in ticket 13 (Metodologi) and fold into map/workflow records.

Pre-edit backup: `.scratch/_backups/spc-full-paper-20261017-1337/19-lampiran.md`.
