# 20: Assemble, review, and package for submission

**What to build:** Assemble all sections into the official template, run the compliance/format
checks and the two-axis review, and export the submission PDF with the prescribed filename.

**Blocked by:** 16, 17, 18, 19 (all sections).

**Status:** blocked — packaging complete and verified; the frozen-boundary criterion fails in the
body text (finding B1) and two content BLOCKERs sit in drafts owned by Load A (B2, B3). Load B
cannot close them without editing drafts 11–16.

- [x] All nine mandatory sections present, in order.
- [x] Format rules pass: Bahasa Indonesia, Times New Roman 12 pt, 1.15 spacing, A4, 2.54 cm
      margins, 10–20 pages, filename `SPC_FullPaper_NamaKetuaTim.pdf`.
- [x] Claim-ledger coverage audit passes — every number maps to a ledger entry.
- [ ] Expectation-label audit passes — no result-shaped statement unlabelled. **Fails on two
      sentences (B3); see below.**
- [x] Forbidden-content check passes — zero glove/IMU, zero analog physical joystick, and no
      "aplikasi web" / "smartphone app" as the described interface.
- [x] Two-axis review (Standards vs Spec) run as parallel sub-agents; findings resolved or recorded.
- [ ] Frozen-boundary check passes — Pendahuluan and the core problem match the Extended Abstract.
      **Fails: draft 12 reverses the Extended Abstract's causal premise (B1).**
- [x] Prior-art honesty check passes — smoothing-is-a-hypothesis and 2-second-hold-is-
      project-defined caveats both present.

## Answer

### Artefacts

| Artefact | Path |
|---|---|
| Assembled paper (Word) | `outputs/SPC_FullPaper_AnargyaArkanDhafyHamdani.docx` |
| Submission PDF | `outputs/SPC_FullPaper_AnargyaArkanDhafyHamdani.pdf` |
| Assembler (re-runnable) | `assemble-full-paper-archonx.py` |
| Compliance checks (re-runnable) | `check-full-paper-archonx.py` |
| PDF export (Word COM) | `.scratch/export-pdf-archonx.ps1` |

The assembler reads the nine section drafts, strips every `Catatan draf (scaffolding …)` block,
strips the internal `-archonx` watermark from headings and prose (the cover uses
`TITLE_SUBMISSION` from `title.md`), and renders the docx on the official template's page setup.
It is deterministic: re-running it reproduces the same document from the drafts.

### Verified state (29 pages total)

Measured from the artefacts, not estimated:

- **Body length 17 pages** (Abstrak p. 2 → end of Kesimpulan dan Saran p. 18), excluding cover,
  Daftar Pustaka (pp. 19–20) and Lampiran (pp. 21–29). Guidebook limit 10–20. PASS.
- **Page geometry:** A4 21.0 × 29.7 cm, margins L/R/T/B exactly 2.54 cm, body Times New Roman
  12 pt, 1.15 line spacing, centred page number from p. 2 (cover suppressed). PASS.
- **Nine sections in guidebook order:** Halaman Sampul → Abstrak → Pendahuluan → Dasar Teori →
  Metodologi → Hasil dan Pembahasan → Kesimpulan dan Saran → Daftar Pustaka → Lampiran. PASS.
- **Fonts:** 536 TNR runs, 115 Courier New runs (code/diagram blocks only), 48 Cambria Math runs
  (equations (1)–(7)). No other font in the document. PASS.
- **Forbidden content:** 0 hits for glove / sarung tangan / IMU / MPU6050 / flex sensor;
  0 hits for aplikasi web / antarmuka web / web joystick / Blynk / smartphone / ponsel pintar;
  0 hits for joystick analog / stik analog fisik; 0 residual `-archonx`. PASS.
- **Citations:** bracketed numbers [1]–[11] contiguous, all eleven present in the bibliography, no
  orphans, no gaps. PASS.
- **Abstract:** one paragraph, 224 words, 5 alphabetical keywords. PASS.
- **Captions:** every table numbered and captioned in 10 pt italic above the table — Tabel 1
  (targets, Hasil), Tabel 2 (task split), Tabel 3 (budget), Tabel 4 (components), Tabel 5–7
  (PS2 pins, PCA9685 pins, PWM channels). PASS.
- **Prior-art honesty:** "Tidak ditemukan bukti langsung bahwa pemulusan perintah semata
  meningkatkan akurasi penempatan" (Dasar Teori) and "project-defined criterion … tidak
  diposisikan sebagai metrik standar telemanipulasi industri" (Metodologi). PASS.

Reproduce with:

```
./.venv/Scripts/python.exe assemble-full-paper-archonx.py
powershell -File .scratch/export-pdf-archonx.ps1
./.venv/Scripts/python.exe check-full-paper-archonx.py    # 17 checks, 0 failures
```

### Two-axis review — what was run and what happened

Two independent sub-agents reviewed the built artefacts in parallel: one on the **Standards** axis
(guidebook, template, rubric, language) and one on the **Spec** axis (spec.md, map.md, tickets,
claim ledger, Extended Abstract). Every finding that could be checked was verified before action;
three review claims were wrong and are recorded as rejected below.

**Fixed in this ticket (assembly layer, `assemble-full-paper-archonx.py`):**

1. Page break before Pendahuluan, Daftar Pustaka and Lampiran (body no longer starts on the
   abstract page).
2. Nested emphasis (`**… (*x*) …**`) renders as italic instead of leaking literal asterisks; long
   bullet continuations are joined so italic spans do not split across paragraphs.
3. Daftar Pustaka entries left-aligned with a 0.9 cm hanging indent — justified entries were
   producing one-word lines against long URLs.
4. `2x2` normalised to `2×2`.
5. Sub-headings promoted to real Heading 3/4 styles, so the document has a usable outline.
6. Captions and paragraphs preceding tables/code blocks set `keep with next`; table rows
   `cantSplit`; header rows repeat across page breaks; column widths reserve enough space that no
   number breaks mid-token (`Rp72/5.000`, `Pera/n`, `Juml/ah` are gone).
7. Code/diagram blocks auto-size (6.5–8.5 pt Courier) so no line runs past the text block.

**Fixed in the Load B drafts (`18-daftar-pustaka`, `19-lampiran`):**

8. **[6] invented co-authors corrected.** The draft carried "J. Yoon, S. Lee, H. Kim, dan S. Oh".
   arXiv:2503.01216**v1** (the cited version) lists J. Yoon, S. Park, H. Park, C. Kim, S. Park,
   M. Hwang. Title and v1 URL were already correct; only the author list was wrong.
9. **[7] invalid DOI removed.** `10.1109/M2VIP61509.2024.10746144` returns "DOI Not Found" at
   doi.org; the IEEE Xplore URL resolves, so the entry keeps the URL and drops the DOI. Author
   list verified correct (Zixiong Wang, Yinlong Zhang, Xin Zhang).
10. **Appendix moved the intervention to the receiver.** Lampiran 3 and the Lampiran 4 diagram put
    the fine-mode gain scaling and the release-to-hold latch on the receiver ESP32, contradicting
    ticket 06 amendment 3. Both now put the three control layers on the sender; the receiver only
    maps the already-scaled command to joint angles, clamps, and updates PWM.
11. Lampiran 5 pseudocode split into `build_packet()` (sender: PS2X read, deadzone, gain α, latch,
    `t_send`) and `process_teleoperation()` (receiver: latency, angle mapping, clamp, PWM).
12. Lampiran 1 claimed the firmware was "dikembangkan dan diuji" in past tense — now "dirancang …
    integrasi dan pengujiannya dijadwalkan pada 18 Oktober 2026", consistent with the integrity
    statement in Hasil dan Pembahasan.
13. Four uncaptioned appendix tables given numbers and captions; Tabel 2/3/4 renumbered into
    appearance order (2 = task split, 3 = budget, 4 = components, 5–7 = pin/channel maps).
14. "Master"/"Slave" removed from the appendix (GLOSSARY avoid-list) → Unit Pengirim / Unit
    Penerima.
15. Diagram labels corrected: "4-wire SPI" → "Serial 4-kawat (polled)"; "Paket UDP / ESP-NOW" →
    "Paket UDP (2,4 GHz)" — the latency argument only holds for one committed transport.
16. Budget prices carry an explicit scope line ("seluruh harga merupakan perkiraan tim per Oktober
    2026 yang belum diverifikasi terhadap tautan pemasok"), not just the PS2 row.
17. **[11] LimpSquid "Robotic arm" Thingiverse citation added & verified.** Sourced original CC BY-NC 4.0
    provenance for the 5-DOF mechanical arm ("proyek Wonder Tiger" retained as team project nickname in prose),
    cited in Lampiran (Tabel 2 & Tabel 4), added as entry [11] in Daftar Pustaka with verified live URLs.
18. **Draft 13 citation cluster whitespace normalized.** Fixed `latensi komunikasi.[8],[9]` to `[8], [9]`.
19. **Checkscript updated.** Citation contiguous check updated from `range(1, 11)` to `range(1, 12)` ([1]–[11]).
20. **Visual verification pass completed.** Rendered pages p10 (Metodologi [8], [9]), p19 (Daftar Pustaka [1]–[10]),
    p20 (Daftar Pustaka [11]), p21 (Lampiran Tabel 2 credit), and p23 (Lampiran Tabel 4 spec credit) visually inspected
    via `vision_analyze`; all confirmed clean with no formatting defects.

**Recorded for Load A (`archonx01`) — body drafts 11–16, not edited by Load B:**

17. **B1 (BLOCKER, draft 12) — frozen-boundary divergence.** Line 21 reads "ketepatan berhenti di
    atas sasaran **tidak lagi ditentukan oleh tangan operator**"; the Extended Abstract states
    verbatim "akurasi ini juga **ditentukan oleh handling dari operator**". Line 26 then
    self-certifies that the background was "dipertahankan tanpa perubahan". Suggested fix: keep
    the EA premise and add the new locus — "akurasi tetap ditentukan oleh mutu penanganan
    operator; pada teleoperasi, mutu itu melewati penerjemahan perintah menjadi gerakan sendi".
18. **B2 (BLOCKER, drafts 11/13/14/15) — internal process files cited inside the submission:**
    `claim-ledger.md` (3×) and "ADR 0001" in a heading. A judge cannot open any of them; the
    surrounding argument stands without them.
19. **B3 (BLOCKER, drafts 13/15) — result voice:** "…sehingga secara efektif memitigasi fenomena
    osilasi koreksi berlebih (hunting)" and "Manipulator berhenti seketika … tanpa mengalami
    pergeseran (drift)". Neither is measured. Fix: "diharapkan memitigasi" / "dirancang agar
    berhenti …; ada tidaknya drift diukur pada tahap Final".
20. **B4 (MAJOR, draft 14) — [1]/[2] swapped in Hasil:** "IAEA-TECDOC-1433 [1] dan IAEA Radiation
    [2]" is inverted; the bibliography has [1] = *Radiation, People and the Environment*,
    [2] = TECDOC-1433.
21. **B5 (MAJOR, draft 14) — 200 ms acquires a psychophysical justification** in Tabel 1 ("Ambang
    batas persepsi kendali semi-real-time operator") that the same section denies two pages
    earlier ("tidak dikutip dari literatur eksternal"). Restate as a team design assumption.
22. **B6 (MAJOR, draft 16) — sample size:** abstract says "tiga pasang operator" (= six people),
    Metodologi says "3 orang operator"; the 480-trial arithmetic only works for three.
23. **B7 (MAJOR, drafts 15/16) — mechanism inverted:** "memperluas rentang gerak fisik stik"
    contradicts Eq. (3), where the same deflection produces a *smaller* joint motion. Fix:
    "meningkatkan resolusi kendali pada rentang gerak stik yang sama".
24. **B8 (MAJOR, draft 14) — citation style** is author-year-plus-bracket in places ("(Richter et
    al. 2019 [4])", "(Akl, Tummala, dan Li (2006) [8])", "[4],[3]"). Reduce to "[n]", ascending.
25. **B9 (MAJOR, drafts 14/15) — "di mana" calque** used four times as an English relative adverb.
26. **B10 (MAJOR, draft 13) — 8-of-10 criterion does not fit a 40-trial cell.** Define the unit
    (e.g. four 10-trial blocks per cell, cell passes at ≥8/10 per block, or ≥32/40).
27. **B11 (MINOR, draft 14) — unanchored design numbers:** foam block "±15 gram", grid reading
    precision "0,5 mm", the millimetre cell pitch. Label as design specifications, or drop.
28. **B12 (MINOR, draft 12) — unsourced risk clause:** "berisiko pada bahan yang ditangani maupun
    pada lingkungan sekitarnya" has no ledger anchor (C8 was deleted).

**Rejected review findings (verified wrong):**

29. *"Insert `skema-rangkaian-teleoperasi-archonx.png` and `flowchart-metodologi-archonx.png` as
    Gambar 1/2."* Both assets are pre-pivot (4 Oct): the schematic shows "5 MPU6050 · analog
    joystick baseline", and the flowchart contains glove calibration plus a two-interface
    comparison. Publishing either would inject the forbidden content this submission must not
    contain. The ASCII block diagram was redrawn this ticket and stays the only diagram until a
    post-pivot figure is produced and approved.
30. *"Reference [3] could not be verified."* MDPI blocked the fetcher; the ledger entry (S10) and
    the author list stand. Not a defect.
31. *"Body is single-column while the template's body section is two-column."* True of the template
    file, but two columns would cut the 17-page body to roughly 9 pages — below the guidebook's
    10-page minimum. Single column is the only compliant choice; recorded as a deliberate
    deviation.

### Downstream actions for the Load A owner (shared files)

- `claim-ledger-archonx.md`: add **S14** (LimpSquid, "Robotic arm", Thingiverse, 2016, CC BY-NC 4.0;
  licence attribution requirement for 5-DOF 3D printed arm). Mark **S5** and **S6** as `SUPERSEDED (antarmuka sarung tangan
  ditinggalkan)`; the paper no longer cites them.
- Budget basis: the ten component prices in Tabel 3 now carry a team-estimate scope line, but the
  ledger holds only C12 (PS2, Rp40k–70k) and C13 (ESP32s owned). Add one ledger entry for the
  budget basis, or the appendix price column stays an in-paper estimate only.
- `issues/03-experiment-protocol.md`: state the trial-block unit behind the 8-of-10 criterion (B10)
  so the Final-stage protocol and the paper cannot drift apart.
- `map.md` → Decisions: ticket 20 assembled the paper; the submission artefact strips the
  `-archonx` watermark; the two pre-pivot figures were rejected as forbidden-content risks.

### Known limits of this artefact

- No figures. The only diagram is the redrawn ASCII block diagram in Lampiran 4.
- Defects B1–B12 are still in the body text of this build; they are recorded, not fixed, because
  drafts 11–16 belong to Load A.
- The PDF is exported through Word COM; a different Word/LibreOffice version may shift the page
  count by ±1. Body length has 3 pages of headroom either way.
