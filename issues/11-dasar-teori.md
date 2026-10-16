# 11: Dasar Teori

**What to build:** Rebuild Dasar Teori on the prior art the intervention actually leans on —
motion scaling and hybrid position/rate control — instead of the old comparison framing, and
state the honesty caveat about smoothing.

**Blocked by:** 08 (GLOSSARY).

**Status:** resolved

- [x] Covers motion scaling (Richter 2019), hybrid position/rate control (Han & Yang 2022; Lee
      2024), and the filtering literature.
- [x] States explicitly that **no direct evidence was found that command smoothing alone improves
      placement accuracy** — smoothing is framed as a hypothesis, not a proven effect.
- [x] Every external claim maps to a sourced entry in `claim-ledger-archonx.md`; no unsourced
      number.
- [x] Uses GLOSSARY vocabulary; no "aplikasi web" / "smartphone app" wording.

## Answer

**Resolved 2026-10-16 (ArchonX).** The section is drafted at
`.scratch/spc-full-paper/draft/11-dasar-teori-archonx.md` (six subsections, Indonesian, house style,
`-archonx` on the main header and every subheader). This also establishes the drafting convention the
remaining section tickets inherit: **one markdown file per section at
`.scratch/spc-full-paper/draft/NN-<slug>-archonx.md`**, assembled into `Full paper/Format Full Paper.docx`
by ticket 20.

### What the section does

Rebuilt on the intervention's actual prior art rather than the rejected comparison framing:

1. why precise placement is the hard part of teleoperation (precision–speed compromise);
2. **motion scaling and hybrid position/rate control** — Han & Yang 2022 (the "bubble" strategy,
   −17,23 % completion time and −34,02 % NASA-TLX), Richter 2019 (positional/velocity scaling, lower
   error at the cost of task time, 16/17 participants), Lee 2024 (variable scaling by task phase,
   described qualitatively), Yoon 2025 (adaptive coarse/fine scaling, −38,46 % clutch / −11,96 % time /
   −58,01 % NASA-TLX);
3. **the filtering literature and its honest limit** — Wang 2024 compares eight filters and reports
   smoother trajectories, **not** a placement-accuracy result;
4. joint mechanics and the command→joint mapping (eqs 1–3);
5. Wi-Fi propagation as the reason distance is a test variable (Akl 2006; Pandey & Parasuraman);
6. why the PS2 pad forces a polling host MCU (PS2X).

### Claim surface extended (the gate needed it)

Ticket 11 requires every external claim to map to a ledger entry, but the prior-art sources lived only
in `research/05-prior-art.md` (ticket 05) — **they were not in `claim-ledger-archonx.md`.** Appended a
dated *"Full-paper additions — prior art for Dasar Teori (ticket 11)"* section grading **S9–S13**
(Richter, Han & Yang, Lee, Yoon, Wang) and claims **C14–C18**, following the precedent ticket 09 set. No
source was invented: every one is carried from the ticket-05 research file with its URL and retrieval
date.

Two evidence caps are enforced in the draft:

- **Lee 2024 (S11) and Wang 2024 (S13) are abstract-level only** (paywalled / IEEE-restricted). Lee is
  therefore described **qualitatively with no number quoted**; the ledger's `Cannot support` lines say so.
- The Wi-Fi figures (S3) and the latency figures (S4) are other setups' numbers — the draft states them
  as mechanism, never as this link's values; the project's latency stays a pre-registered target.

### Honesty caveat (the section's load-bearing sentence)

> **Tidak ditemukan bukti langsung bahwa pemulusan perintah semata meningkatkan akurasi penempatan.**

Followed immediately by the design consequence: fine mode is **not** a filter and is not presented as
one — it lowers the command gain, and the claim is limited to what the team will measure.

### Decisions taken while drafting (flagged, not silent)

- **Equation numbering.** Dasar Teori owns eqs (1) torque, (2) coarse mapping, (3) the new fine-mode
  gain-reduction equation. The latency equation and the statistics equations (the abstract's (3)–(6))
  therefore renumber when Metodologi/Hasil are drafted (tickets 13/14) and are finalised at assembly
  (ticket 20). `spec.md`'s "eqs (4)–(6) unchanged" referred to *those equations' content*, which is
  unchanged; their numbers shift because a new equation entered ahead of them. Recorded so ticket 20 does
  not treat the shift as drift.
- **Citation numbering is provisional.** Pendahuluan keeps the IAEA sources as [1]–[2]; Dasar Teori
  starts at [3] and runs to [10]. Final numbering belongs to ticket 18 (Daftar Pustaka) / ticket 20. The
  draft carries a scaffolding block (marked *hapus saat perakitan*) mapping each `[n]` to its ledger ID.
- **eq (2) written device-agnostically.** It no longer names a sensor angle — the committed paradigm is
  PS2 **stick rate** control, so the input is a normalised operator displacement `u` and `G` is the
  command-to-joint gain. Exactly the "relabelled baseline coarse mapping (device-agnostic)" that
  `spec.md` and ticket 04's amendment call for.

### Verification run (executed, not re-read)

A Python check over the draft and the ledger returned:

- prior-art coverage: Richter, Han, Lee, Yoon, Wang, penskalaan gerak, kendali hibrida, pemulusan — all present;
- honesty caveat: exact sentence present, `hipotesis` present;
- forbidden content: `aplikasi web` 0 · `smartphone app` 0 · `glove` 0 · `IMU` 0 · `sarung tangan` 0 ·
  `joystick` 0;
- ledger inventory: **13 S entries** (S1–S13), **18 C entries** (C1–C18) — the five new S and five new C
  are present;
- glossary vocabulary: `mode posisi-halus`, `stik`, `pengendali PS2`, `sendi`, `gripper`,
  `pra-registrasi`, `target` — all present;
- watermark: every `#` header ends `-archonx`.

Pre-edit backups: `.scratch/_backups/spc-full-paper-20261016-2158/` (this ticket, `claim-ledger-archonx.md`,
`map.md`, `WORKFLOW-paper-development.md`).
