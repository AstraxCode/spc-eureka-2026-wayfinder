# 16: Abstrak

**What to build:** The Indonesian abstract, written last, reframed to the solution: the
contribution is the fine-positioning intervention; the 2×2 protocol is presented as planned
validation; every result-shaped statement is labelled an expectation.

**Blocked by:** 11, 12, 13, 14, 15 (all body sections it summarises).

**Status:** resolved

- [x] Contribution stated as the fine-positioning intervention; 2×2 presented as planned validation.
- [x] Every result-shaped statement labelled an expectation.
- [x] No "aplikasi web" / "smartphone app" wording.
- [x] Consistent with every drafted section (no claim the sections don't support).

## Answer

### Section draft created
The section is drafted and saved at `.scratch/spc-full-paper/draft/16-abstrak-archonx.md`
(3,526 characters, 2 markdown headers, both ending with the required internal watermark `-archonx`).

### Structure and template compliance
1. **Paragraph count and word length:**
   - Follows `Full paper/Format Full Paper.docx` template line 32: written in exactly one single continuous paragraph of 224 words (strictly within the required 150–250 word limit).
2. **Keywords:**
   - Exactly 5 alphabetical keywords/phrases adhering to template line 33 (3–5 items, alphabetical order):
     *faktor reduksi gain, lengan robot 5-DOF, mode posisi-halus, penanganan bahan radioaktif, teleoperasi stik PS2*.
3. **Contribution and solution framing:**
   - Framed around the fine-positioning intervention (*mode posisi-halus*) via physical PS2 stick rate control and dual ESP32 over 2.4 GHz Wi-Fi UDP.
   - Highlights the trigger-toggled gain reduction factor $\alpha$ ($0 < \alpha < 1$) and the inherent *release-to-hold* natural locking mechanism without hardware clutches.
4. **Validation protocol as planned pre-registration:**
   - The 2×2 factorial design (coarse vs fine mode, 1 m vs 3 m distances, 3 paired operators, 40 trials/condition) manipulating 30 mm synthetic foam cubes on a calibrated millimeter grid is explicitly presented as a planned pre-registered validation protocol.
5. **Academic integrity and expectation labelling:**
   - Every result-shaped metric (one-way latency $\le 200$ ms, Euclidean error within 1 grid cell, 2-second hold at $\ge 80\%$ success) is explicitly stated as pre-registered design targets and engineering expectation analyses, adhering to Eureka! ITB 2026 Guidebook p. 5 item 7 with respect to the 18 October 2026 physical prototype build milestone.
6. **No prohibited strings:**
   - Zero occurrences of prohibited interface terms (per `spec.md` Testing Decisions check 7).
7. **Consistency with all body sections:**
   - Grounded entirely in tickets 11–15; no new claims or ungrounded assertions introduced.

### Programmatic verification
- Header watermark check: 2 of 2 headers end with `-archonx` (100%).
- Abstract paragraph word count: 224 words (within 150–250 range).
- Prohibited terms check: 0 occurrences of prohibited terms (`glove`, `sarung tangan`, `IMU`, `MPU6050`, `aplikasi web`, `smartphone app`, `Blynk`).
- Keywords check: 5 keywords, strictly sorted alphabetically.
- Format check: 0 citations, 0 equations, 0 tables, 0 figures in abstract body.
