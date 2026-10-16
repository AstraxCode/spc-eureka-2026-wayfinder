# Title source (single place) — the expand–contract title file-archonx

**This file is the only place the paper title is written.** Every artefact that shows the title
(Halaman Sampul / ticket 17, the Abstrak header, any spec or ticket reference) draws its text from
here. To change the title, edit the two `TITLE_*` lines below and nowhere else — no rewrite is
forced anywhere else in the paper.

## The title

TITLE_INTERNAL: Mode Posisi-Halus Berbasis Stik PS2 untuk Akurasi Penempatan Lengan Robot Teleoperasi 5-DOF pada Penanganan Bahan Radioaktif-archonx

TITLE_SUBMISSION: Mode Posisi-Halus Berbasis Stik PS2 untuk Akurasi Penempatan Lengan Robot Teleoperasi 5-DOF pada Penanganan Bahan Radioaktif

- `TITLE_INTERNAL` is the working title, carrying the `-archonx` watermark convention (see
  `GLOSSARY.md` → Working conventions). It is used on internal documents and drafts.
- `TITLE_SUBMISSION` is the text printed on the submitted cover page: identical, with the
  `-archonx` watermark suffix stripped (user decision, 16 Oct 2026).

## Provenance

Chosen **16 Oct 2026** by the user (Acting as the team's decision point) in wayfinder ticket
`issues/10-final-title.md`, from four solution-framed Indonesian candidates. It closes the last
open item on `map.md` and GitHub Issue #1.

The pre-PS2 draft title is **void**: it named the superseded screen-based interface. The title must
carry none of the prohibited interface strings listed in `spec.md` → Testing Decisions, check 7
(they are deliberately not spelled out here, following the ticket-08 precedent, so this file stays
clean for the ticket-20 forbidden-content grep).

## Constraints this title satisfies (ticket 04 / ticket 10)

- Indonesian, solution-framed: names the designed solution (mode posisi-halus) and the committed
  PS2-stick control paradigm, not a joystick-vs-glove comparison.
- Committed paradigm: **stik PS2** (stick = multi-DOF rate control, ABXY = single joint, trigger =
  fine mode).
- Carries none of the prohibited interface strings (spec.md Testing Decision 7).
- The 14 Oct admin ruling is respected: title edits were allowed; Pendahuluan and the core problem
  are not touched by this ticket.
