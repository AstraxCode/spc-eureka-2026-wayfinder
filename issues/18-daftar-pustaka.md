# 18: Daftar Pustaka

**What to build:** The bibliography, built from the claim ledger's sourced entries.

**Blocked by:** 11, 12, 13, 14, 15 (the citing sections).

**Status:** resolved

- [x] Every citation used in the draft appears; every entry is real and matches its ledger source.
- [x] IEEE-style format per the official template.
- [x] No fabricated entries and no duplicates.
- [x] Every ledger-sourced claim is cited; ledger entries with no corresponding citation are
      removed or the claim is added.

## Answer

**Resolved 2026-10-17 (ArchonX).** Draft: `.scratch/spc-full-paper/draft/18-daftar-pustaka-archonx.md`
(10 numbered entries, IEEE style per `Full paper/Format Full Paper.docx`, `-archonx` on every header,
scaffolding section detailing claim mapping and ledger alignment).

### Citation numbering & appearance order

All upstream citing sections (11, 12, 13, 14, 15) are `resolved`. An automated audit across the full text
reveals that citations appear in strictly contiguous order [1] through [10] across sections 12 (Pendahuluan)
and 11 (Dasar Teori), with subsequent sections (13 Metodologi, 14 Hasil dan Pembahasan) re-citing within
this closed set:

1. `[1]` = IAEA, *Radiation, People and the Environment* (2004) — First cited in Pendahuluan (lines 8, 11).
   Supports C1 (dose limits) and C2 (DNA ionizing radiation risk). Ledger source: **S2**.
2. `[2]` = IAEA, *Remote Technology Applications in Spent Fuel Management*, IAEA-TECDOC-1433 (2005) —
   First cited in Pendahuluan (line 17). Supports C3 (remote systems cut worker dose). Ledger source: **S1**.
3. `[3]` = J. Han & G.-H. Yang, *Applied Sciences* (2022) — First cited in Dasar Teori (line 24).
   Supports C14 (position-rate hybrid control & "bubble" strategy). Ledger source: **S10**.
4. `[4]` = F. Richter, R. K. Orosco, & M. C. Yip, *ICRA* (2019) — First cited in Dasar Teori (line 44).
   Supports C15 (motion scaling under delay). Ledger source: **S9**.
5. `[5]` = H. Lee, J. Han, & G.-H. Yang, *IJCAS* (2024) — First cited in Dasar Teori (line 51).
   Supports C16 (variable scaling framework, cited qualitatively at abstract level). Ledger source: **S11**.
6. `[6]` = J. Yoon et al., *arXiv:2503.01216* (2025) — First cited in Dasar Teori (line 56).
   Supports C17 (adaptive coarse/fine motion scaling). Ledger source: **S12**.
7. `[7]` = Z. Wang, Y. Zhang, & X. Zhang, *IEEE M2VIP* (2024) — First cited in Dasar Teori (line 73).
   Supports C18 (comparative filter study; baseline for the honesty caveat on smoothing). Ledger source: **S13**.
8. `[8]` = R. Akl, D. Tummala, & X. Li, *Univ. of North Texas Tech. Rep.* (2006) — First cited in Dasar Teori (line 119).
   Supports C5 (log-distance Wi-Fi path loss). Ledger source: **S3**.
9. `[9]` = P. Pandey & R. Parasuraman, *arXiv:2110.03011* (2021) — First cited in Dasar Teori (line 124).
   Supports C6 (Wi-Fi latency and jitter distributions in mobile robotics). Ledger source: **S4**.
10. `[10]` = B. Porter, *madsci1016/Arduino-PS2X* (ported for ESP32 by *MyArduinoLib*) — First cited in Dasar Teori (line 137).
    Supports C11 (PS2 four-wire synchronous polling protocol requiring sender MCU). Ledger source: **S8**.

### Claim ledger reconciliation (staged for assembly / Load A)

Per Load B shared-file discipline, `claim-ledger-archonx.md` is read-only for `archonx`. The following audit is recorded here for assembly at Ticket 20:

- **11 active external claims cited:** C1, C2, C3, C5, C6, C11, C14, C15, C16, C17, C18 are 100% cited in the draft text and map directly to entries `[1]`–`[10]`.
- **C4:** Contradicted in ledger; reframed as an intentional scope limitation (no citation).
- **C8:** Removed per user decision on 16 Oct (unsupported causal chain).
- **C9, C10, C12, C13:** C9 was the initial glove hypothesis (eliminated); C10 is the team's experimental test protocol; C12/C13 are team budget estimates and inventory. None requires an external bibliographic citation.
- **S5 & S6 (Zhou et al., Jia et al.):** Sourced during the initial Extended Abstract phase for the glove-vs-joystick comparison. Following the pivot to the fine-positioning PS2 controller intervention (ADR 0002, Tickets 04/06/09/11/12), the interface comparison was eliminated from the Full Paper. As required by acceptance criterion 4 ("ledger entries with no corresponding citation are removed or the claim is added"), S5 and S6 are flagged to be marked as *SUPERSEDED (glove interface eliminated)* in `claim-ledger-archonx.md` upon final assembly.
- **S7 (Fuji Electric):** Marked *UNVERIFIED* in ledger; excluded from Daftar Pustaka.

### Verification suite results

An automated verification script (`verify_ticket_18.py`) was executed against the draft text:
- Header check: All headers end with `-archonx` (depths `#` and `##`).
- Entry count & sequence: Exactly 10 entries `[1]`–`[10]` in strict contiguous sequence.
- Duplication check: 0 duplicate entries.
- Draft-to-bibliography alignment: Every citation `[1]`–`[10]` in body drafts (sections 11–16) resolves to a real entry in `18-daftar-pustaka-archonx.md`.
- Appearance order: First-appearance sequence across all sections is strictly `[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]`.
- Formatting: All entries strictly follow IEEE bibliography style per competition guidelines with authors, titles, publication/proceedings names, page ranges/report numbers, dates, and live URLs/DOIs.
