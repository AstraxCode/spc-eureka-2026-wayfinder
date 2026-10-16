# Claim Ledger — SPC Eureka! ITB 2026 Extended Abstract-archonx

Project: Teleoperated robotic arm 🦾 (glove vs joystick, Wi-Fi, tabletop)
Draft under review: `Obsidian Vault/The Board/Teleoperated robotic arm 🦾/Protoabstract.md` → "Pendahuluan mark 3"
Compiled: 2026-09-29 (WIB)
Deadline: Extended Abstract due 30 September 2026, WIB.

---

## Retrieval tools and status-archonx

| Tool | Target | Result |
|---|---|---|
| `web_extract` (built-in) | 3 PDFs (IAEA ×2, UNT) | OK — full text cached locally |
| `COMPOSIO_SEARCH_WEB` (Exa) | 7 queries | OK — 7/7 succeeded |
| `COMPOSIO_SEARCH_FETCH_URL_CONTENT` (Exa) | 4 HTML pages | OK |
| `web_extract` (built-in) | 4 HTML pages | 3/4 OK; MDPI failed `document_antibot` |
| `FIRECRAWL_SCRAPE` | 4 pages (2 PDF + 2 HTML) | 4/4, `statusCode: 200`. **Cost 245 credits** |
| `FIRECRAWL_CREDIT_USAGE_GET` | account | `remainingCredits: -89` |
| Defuddle `defuddle.md` | arXiv HTML ×3 | OK |
| Defuddle `defuddle.md` | IAEA PDFs ×2 | Failed: `Not an HTML page (content-type: application/pdf)` |
| Defuddle `defuddle.md` | `nrc.gov` page | Failed: origin returned 403 |
| `web_search` (built-in, Firecrawl backend) | cladding query | Failed twice — backend `Converting circular structure to JSON`, keyless `403 Forbidden` |

**Firecrawl account is now over limit.** Started at 156 remaining; this run consumed 245 (158 + 85 + 1 + 1). Balance `-89`. Billing period resets 2026-09-30T14:44 UTC (≈ 30 Sep, 21:44 WIB). Further Firecrawl scrapes will fail until then. Use `web_extract` and Defuddle meanwhile.

---

## Source inventory-archonx

### S1 — IAEA-TECDOC-1433 — Grade C
IAEA, *Remote technology applications in spent fuel management*, IAEA, Vienna, 2005.
URL: https://www-pub.iaea.org/MTCD/Publications/PDF/TE_1433_web.pdf
Retrieval: `web_extract` (380,768 chars) + Firecrawl `statusCode 200`, 158 pages.
**Full text read** (foreword, contents, section 5–6 extract). Grade C: intergovernmental technical document, not peer-reviewed.

Verbatim (foreword, whitespace normalized):
> "Remote systems technology has been extensively applied to a variety of work in spent fuel management facilities with such benefits as dose reduction to workers, enhancement of operational performance or reliability, saving of labor costs, etc. Remote systems are an integral part of facilities for work to be carried out inside shielding and/or containment enclosures engineered to protect workers and the environment from hostile radioactive sources like spent nuclear fuel or radioactive wastes."

**Supports:** remote systems in spent fuel handling exist and are justified by worker dose reduction.
**Cannot support:** any claim that remote refueling is unsolved, or that a tabletop arm addresses refueling.

### S2 — IAEA, Radiation, People and the Environment — Grade C
IAEA, *Radiation, People and the Environment*, IAEA/PI/A.75/04-00391, Vienna, February 2004. 85 pp.
URL: https://www.iaea.org/sites/default/files/radiation0204.pdf
Retrieval: `web_extract` (187,394 chars) + Firecrawl `statusCode 200`.
**Full text read** (ch. 1, 5–6 passages).

Verbatim:
> "Free radicals are highly reactive chemically and can alter important molecules in the cell. One particularly important molecule is deoxyribonucleic acid, DNA, found mainly in the nucleus of the cell."

> "Radiation may ionize a DNA molecule leading directly to a chemical change, or the DNA may be changed indirectly when it interacts with a free [radical] … the chemical change can cause a harmful biological effect leading to the development of cancers or inherited genetic defects."

> "The BSS specify dose limits for workers of 20 mSv per year (averaged over a five-year period, with no more than 50 mSv in any year) and for members of the public of 1 mSv in a year."

> "Analysis by UNSCEAR shows that the average annual dose to workers from man-made sources is 0.6 mSv"

**Supports:** ionizing radiation → DNA damage → cancer; existence and size of occupational dose limits.
**Cannot support:** that *gamma from uranium* is the relevant emitter. The text says "ionizing radiation" generally. Do not attribute to uranium specifically.

### S3 — Akl, Tummala, Li — Indoor Propagation 2.4 GHz — Grade B
R. Akl, D. Tummala, X. Li, *Indoor Propagation Modeling at 2.4 GHz for IEEE 802.11 Networks*, Univ. of North Texas, 2006.
URL: https://digital.library.unt.edu/ark:/67531/metadc30827/m2/1/high_res_d/Akl-2006-Indoor_Propagation_Modeling_at_2.4.pdf
Retrieval: `web_extract` (24,955 chars). **Full text read.**
Venue not confirmed → grade B pending, verify publication venue before citing.

Verbatim:
> "Both theoretical and measurement based propagation models indicate that average received signal power decreases logarithmically with distance."

> "The values of n range from 1.2 (Waveguide effect) to 8. For example, in free space, n is equal to 2, and when obstructions are present, n will have a larger value."

> "Indoor channels are highly dependent upon the placement of walls and partitions within the building."

Model (their eq. 1):
`PL(dB) = PL(d₀) + 10·n·log₁₀(d/d₀) + X_σ`, where `X_σ` is zero-mean Gaussian, std `σ`.

**Supports:** distance and walls change received signal power — the physics behind tujuan 2.
**Cannot support:** what happens to *your* link. `n` and `σ` are environment-specific; you must measure.

### S4 — Pandey & Parasuraman — Wi-Fi on mobile robots — Grade B (preprint)
P. Pandey, R. Parasuraman, *Empirical Analysis of Bi-directional Wi-Fi Network Performance on Mobile Robots in Indoor Environments*, arXiv:2110.03011.
URL: https://arxiv.org/abs/2110.03011 · https://ar5iv.labs.arxiv.org/html/2110.03011
Retrieval: `web_extract` (50,909 chars) + Firecrawl 200 + Defuddle (HTML OK).
**Abstract, introduction and results tables read**; arXiv preprint, not confirmed peer-reviewed.

2.4 GHz tables (robot **moving**, Table II):

| Case | Throughput M±std (Mbps) | Delay M±std (ms) | %loss | RSSI robot (dBm) | Retransmits |
|---|---|---|---|---|---|
| 1 (Router) | 12.8 ± 3.6 | 47.8 ± 37.7 | 0 | −57.5 ± 7.4 | 2376 |
| 3 (Robot-AP) | 19.1 ± 4.3 | 163.6 ± 270.7 | — | — | — |

Robot **stationary** (Table III), 2.4 GHz delay only: Case 1 = 46.4 ± 34.9 ms · Case 7 = 106.3 ± 105.1 ms · Case 9 = 107.6 ± 82.8 ms.

Verbatim:
> "we omit the measurement of packet loss, which is not a real-time measurement of channel quality as it requires a reasonable amount of time (a few seconds) and a static environment (so it does not apply to a mobile robot context)."

**Supports:** Wi-Fi network delay in robot teleoperation is tens to hundreds of ms, and varies strongly with access-point placement and link conditions — often with standard deviation larger than the mean.
**Cannot support:** your latency. Different hardware, AP, ROS stack. Column mapping is from a flattened markdown table; re-check against the PDF before quoting numbers.

### S5 — Zhou, Hou, Baraka — VR vs SpaceMouse — Grade B (preprint)
Y. Zhou, M. Hou, K. Baraka, *Static Is Not Enough: A Comparative Study of VR and SpaceMouse in Static and Dynamic Teleoperation Tasks*, arXiv:2601.13042, 19 Jan 2026.
URL: https://arxiv.org/html/2601.13042v1
Retrieval: `web_extract` (41,502 chars). **Abstract + introduction read; full body cached, not reviewed.**

Verbatim (abstract):
> "Results show statistically significant advantages for VR: higher success rates, particularly on dynamic tasks, shorter successful execution times across tasks, and earlier successes across attempts, with significantly lower workload and higher usability."

Design: within-subjects, N = 25, two static + two dynamic tasks. Metrics: success rate, task duration, cumulative success, NASA-TLX, SUS.

**Supports:** interface choice measurably changes success rate and completion time — your metric family (mm / detik / persen) matches published practice.
**Cannot support:** which interface wins for you.

### S6 — Jia, Zhou, Zhang — wearable vs haptic device — Grade B (preprint)
J. Jia, H. Zhou, X. Zhang, *An Agile Large-Workspace Teleoperation Interface Based on Human Arm Motion and Force Estimation*, arXiv:2410.15414, 20 Oct 2024.
URL: https://arxiv.org/html/2410.15414v1
Retrieval: `web_extract` (38,828 chars) + Firecrawl 200 + Defuddle. **Abstract + introduction read; body cached, not reviewed.**

Verbatim (abstract):
> "Seven subjects are invited to complete three different tasks: free motion, handover, and pick-and-place action (each task ten times), and the total number of tests is 420. Objectively, we used the task completion time and success rate to compare the performance of the two interfaces quantitatively. … The results showed that the proposed interface achieved a competitive performance with a better operating experience."

**Supports:** the wearable-vs-device comparison design, with exactly your metrics, run as a controlled experiment.
**Cannot support:** that a wearable beats a joystick. The finding is *"competitive"*, not superior. **This is disconfirming evidence** against any assumption that the glove will win.

### S7 — Fuji Electric — Grade C, UNVERIFIED
Fuji Electric, *Remote handling | Three core technologies*.
URL: https://www.fujielectric.com/products/energy/nuclear/product_series/technology_remotehandling.html
Retrieval: **search snippet only.** Claimed text: "positioning several hundred tons of heavy materials with about 1 mm precision by fully remote control".
**Not full-text verified. Do not quote until the page is fetched.**

---

## Claim ledger-archonx

| # | Claim in your draft | Status | Evidence | Confidence | Where it goes |
|---|---|---|---|---|---|
| C1 | Radiation dose at nuclear plants must be reduced to avoid harm | **VERIFIED** | S2 — BSS limit 20 mSv/yr workers, 1 mSv/yr public | High | Pendahuluan **Evidence** slot |
| C2 | Radiation damages DNA → cancer | **VERIFIED** | S2 — ionization direct/indirect, "development of cancers or inherited genetic defects" | High | Pendahuluan **Explanation** |
| C3 | Remote handling lets operators stay at safe distance | **VERIFIED** | S1 — "dose reduction to workers … inside shielding and/or containment enclosures" | High | Pendahuluan **Link** |
| C4 | Remote handling is *unsolved* / reactors can't be refueled remotely | **CONTRADICTED** | S1 + S7 (snippet) — remote fuel handling is established practice | High | **Delete.** Reframe as limitation. |
| C5 | Distance and walls degrade Wi-Fi signal | **VERIFIED** | S3 — log-distance path loss, n = 1.2–8, free space n = 2 | High | Section 2 + tujuan 2 |
| C6 | Wi-Fi link conditions change latency | **VERIFIED (S4)** | S4 — 46 ms to 164 ms mean, std up to 271 ms | Med (their setup) | Section 2 / methodology |
| C7 | Interface choice changes success rate and time | **VERIFIED** | S5, S6 | High | Pendahuluan **Link** → tujuan |
| C8 | Dropped fuel rod → casing damage → gamma leak | **NOT FOUND** | No source obtained (search backend failed twice) | — | **Do not state as fact** |
| C9 | Glove is more accurate than joystick | **OPEN** | S6 finds only "competitive" | — | Hypothesis, not a finding |
| C10 | Your arm's accuracy in mm, time in s, success %, latency vs distance | **YOUR DATA** | — | — | Must come from your experiment |

### PEEL slot mapping-archonx

```
Block 1  Point      ← "dosis perlu dikurangi"                (keep)
         Evidence    ← C1: BSS limits 20 mSv/yr              (REPLACE "refueling adalah contoh")
         Explanation ← C2: DNA ionisasi → kanker             (keep, drop "uranium")
         Link        ← C3: remote systems cut dose → arm     (keep)

Block 2  Point      ← "penanganan butuh akurasi"             (keep)
         Evidence    ← C8 GAP: casing chain UNSOURCED        (REWRITE or delete)
         Explanation ← failure mechanism                     (rewrite with source)
         Link        ← C7: interface affects performance     (good — keep)

Block 3  Point      ← currently a list of 6 concepts         (MOVE to section 2)
         Evidence/X  ← C5 + C6 mechanism, then your data
         Link        ← theme + C4 limitation
```

---

## Claims that must come from your own experiment-archonx

Never state these as achieved before the data exists:

- Placement error in mm (glove vs joystick)
- Task completion time in seconds
- Success rate in percent (state trial count — ≥10 per interface)
- End-to-end latency in ms at each distance/room condition
- Packet loss or retransmit count per condition
- Safe shutdown time after Wi-Fi loss

Pre-registered targets are fine if labelled as targets: *"target ≤ 200 ms"*, not *"beroperasi tanpa latensi yang signifikan"*.

---

## Gaps and retrieval limitations-archonx

1. **C8 (fuel rod / casing) — no source.** `web_search` returned empty, then failed twice with a Firecrawl backend error (`Converting circular structure to JSON`; keyless `403` on `api.firecrawl.dev/v2/search`). No evidence obtained. Either find a source or delete the sentence.
2. **MDPI open-access paper** (`mdpi.com/2624-6511/8/4/105`) — `document_antibot`, not captured.
3. **Defuddle** is HTML-only by design; it cannot read the two IAEA PDFs.
4. **Firecrawl over limit** (`-89`); resets 30 Sep 2026, 14:44 UTC.
5. **S7 not full-text verified** — snippet only.
6. **S5/S6 bodies not read** — abstracts and introductions only. Do not attribute methods or numbers from their bodies without reading them.

---

## Recommended next actions-archonx

1. Replace Block 1's Evidence with the IAEA dose limit (C1). It is sourced, it is stronger, and it makes the Point non-circular.
2. Delete or source Block 2's casing-leak chain (C8). Unverified claim in the first page is the single biggest integrity risk.
3. Move Block 3's physics inventory into section 2 (Konsep Dasar dan Ide Solusi). Pendahuluan needs one bridge sentence, not six concepts.
4. Rewrite tujuan 2 to measure, not promise: *"mengukur latensi jaringan end-to-end dalam ms dan galat penempatan dalam mm pada tiga jarak yang berbeda."*
5. Add S1, S2, S3, S4, S5, S6 to Daftar Pustaka using the guidebook's numbered format. Full Paper's Sistematika Penulisan (10%) grades "penggunaan referensi" — pre-paying it costs nothing.

---

## Full-paper additions — the PS2 pivot (added 2026-10-16, ticket 09)

The 15 Oct PS2 pivot introduced claims this September ledger does not carry. They are graded and
added here because `spec.md` makes this file the gate for the full paper too: nothing enters the
paper that the ledger does not carry.

### S8 — PS2X library for ESP32 — Grade C (community code repository)
MyArduinoLib, *Arduino-PS2X-ESP32* — a fork of madsci1016/Arduino-PS2X (Bill Porter's canonical PS2X
library) adding ESP32 support; ships `examples/PS2X_Example_ESP32/PS2X_Example_ESP32.ino`.
URL: https://github.com/MyArduinoLib/Arduino-PS2X-ESP32 · upstream: https://github.com/madsci1016/Arduino-PS2X
Retrieval: `web_extract`, 2026-10-16. **Repo listing + README read.**
Grade C: community code, 26 stars / 8 forks, not peer-reviewed and not a datasheet — it documents
*usage*, not the pad's electrical protocol.

**Supports:** a PS2 pad is a **polled peripheral**. The library configures it over four signal pins
(clock, command, attention/select, data), and the host MCU reads every button and stick state from
it — the pad originates no traffic of its own and cannot be read without a host MCU. It also
confirms a public ESP32-capable port exists (the fork's README: the upstream did not support ESP32;
the change is `#ifdef ESP8266` → `#if defined(ESP8266) || defined(ESP32)`).
**Cannot support:** any polling-rate, latency or jitter figure — none is stated in the source, and
none may be written down before the team measures it.
**Dead source — do not cite:** the pitch doc also cites an electropeak tutorial
(`electropeak.com/learn/interfacing-ps2-wireless-controller-with-arduino/`). Fetched 2026-10-16:
**HTTP 404, page not found.** It must not enter Daftar Pustaka.
**Prefer for citation:** the canonical upstream (`madsci1016/Arduino-PS2X`; Bill Porter's PS2X
library, billporter.info) for the library claim; the ESP32 fork only as the port actually used.

| # | Claim in your draft | Status | Evidence | Confidence | Where it goes |
|---|---|---|---|---|---|
| C11 | A PS2 controller cannot transmit on its own; it must be polled by a host MCU, so the sender-side ESP32 is required | **VERIFIED (architecture)** | S8 — four-wire polled interface; ESP32 port exists | High (that a host is required) / Med (this fork) | Metodologi architecture; Feasibility |
| C12 | Wired PS2 clone controller price Rp40k–70k | **TEAM ESTIMATE — no listing** | `map.md` price fact (16 Oct); the only live-verified figure is wireless at Rp85k+ (Tokopedia sweep, 15 Oct) | Low | Feasibility, **only with the team-estimate label** |
| C13 | The sender-side ESP32 adds no purchase cost | **INTERNAL — inventory, not external evidence** | ticket 06 criterion 2 / `map.md`: the team owns 2x ESP32 | High | Feasibility |
