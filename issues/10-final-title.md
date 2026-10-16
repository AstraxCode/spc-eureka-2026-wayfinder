# 10: Finalise the paper title (closes GitHub Issue #1)

**What to build:** Finalise the paper title against ticket 04's constraints and close the last
open wayfinder item. The working title stays deliberately TEMPORARY until this lands, and the
paper proceeds past it (user authorised 16 Oct).

**Blocked by:** None (can start immediately — needs teammate/user input; provisional until then).

**Status:** resolved

**Claimed 2026-10-16 (ArchonX).** Title chosen by the user the same day. Pre-edit backup at
`.scratch/_backups/spc-full-paper-20261016-2147/`.

- [x] Title is Indonesian, solution-framed, and satisfies ticket 04's constraints (committed PS2
      control paradigm; Pendahuluan + core problem untouched).
- [x] Title contains no "aplikasi web" / "smartphone app"; carries the `-archonx` internal
      watermark convention.
- [x] The chosen title is stored in **exactly one place** (expand–contract) so the substitution
      forces no rewrite.
- [x] Ticket 04's remaining open item is closed and GitHub Issue #1 is closed with the chosen title.

## Answer

**Resolved 2026-10-16.**

### The title

Held in **`.scratch/spc-full-paper/title.md`** — the single source (mirror: `title.md`). That file
carries two marker lines: `TITLE_INTERNAL` (the working title, with the `-archonx` watermark suffix)
and `TITLE_SUBMISSION` (the cover-page form — the same text with the suffix stripped). Neither form
is repeated anywhere else, so the title is substituted by one edit in one file.

Chosen by the user on 16 Oct 2026 from four solution-framed Indonesian candidates put to them during
this ticket. The `-archonx` suffix is an **internal convention only** — the user ruled it must not
appear on the submitted cover page.

### Why this title

- It names the **solution** (mode posisi-halus) and the **committed control paradigm** (stik PS2),
  so the title reads as a designed intervention, not the superseded web/app-vs-glove comparison.
- It keeps the locked background clause ("pada Penanganan Bahan Radioaktif") continuous with the
  Extended Abstract, so the Pendahuluan and the core problem do not have to move.
- It contains no "aplikasi web" / "smartphone app" wording (the PS2 pivot voids the old draft
  title for exactly this reason).

### Where the title now lives (expand–contract)

New file **`.scratch/spc-full-paper/title.md`** (mirror: `title.md`) is the **single source**. It
holds two machine-substitutable lines, `TITLE_INTERNAL` and `TITLE_SUBMISSION`, plus the
provenance and the constraints list. Ticket 17 (Halaman Sampul) and the Abstrak header draw their
title text from this file; changing the title is one edit here and forces no rewrite elsewhere.

### Verification actually run

1. **Single-source uniqueness** — the anchored marker grep
   `grep -rn '^TITLE_INTERNAL:\|^TITLE_SUBMISSION:' .` returns exactly **2 hits, both in
   `title.md`**. The title value appears in no other file in the effort tree (map/spec/tickets name
   the *file*, not the string).
2. **Constraint greps on the stored lines only** — the two `TITLE_*` lines were tested directly:
   the prohibited interface strings are absent, `-archonx` occurs on `TITLE_INTERNAL` only, and
   `TITLE_SUBMISSION` is `TITLE_INTERNAL` minus that suffix (verified by string comparison).
3. **Ticket 04 open item** — ticket 04's remaining-open line now carries a dated amendment
   pointing at this ticket and `title.md`.
4. **Map** — the title is recorded in `Decisions so far`; `map.md` `Status:` flipped from `open`
   to `closed`, since the title was the last open item.
5. **GitHub Issue #1** — commented with the decision, then closed; verified by reading the issue
   back (`gh issue view 1 --json state` → `CLOSED`).

### Side effect recorded (not silently applied)

The title's Indonesian term **"Mode Posisi-Halus"** conflicts with `GLOSSARY.md` (ticket 08),
which had fixed the Indonesian paper term for fine mode as **"mode halus"**. The title is the
user's decision, so the glossary follows it: the Fine mode entry now records
*Indonesian paper term: **mode posisi-halus** (short form *mode halus*)*. Recorded as a dated
amendment in ticket 08's file, not a silent edit.

### Carried forward (not part of this ticket)

- The wired-PS2 price stays a **team estimate** (Rp40k–70k) until a real listing link is captured.
- Does the arm physically exist as a built prototype? — still a team question; Hasil dan
  Pembahasan wording depends on it.

