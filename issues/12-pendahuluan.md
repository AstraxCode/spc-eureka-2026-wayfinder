# 12: Pendahuluan

**What to build:** Pendahuluan retaining the radiation/accuracy-and-handling background in
substance, with the old glove/app comparison demoted to motivation for the control-side gap.
The background and core problem are frozen by the 14 Oct admin ruling.

**Blocked by:** None (can start immediately).

**Status:** resolved

- [x] Background matches the Extended Abstract **in substance** (frozen-boundary check passes).
- [x] The old comparison appears only as motivation for the gap being addressed — never a results
      section.
- [x] Core-problem statement unchanged (admin ruling 14 Oct).
- [x] No unsourced claims; no "aplikasi web" / "smartphone app" as the described interface.

## Answer

**Resolved 2026-10-16 (ArchonX).** Draft: `.scratch/spc-full-paper/draft/12-pendahuluan-archonx.md`
(509 words, six paragraphs + the three-item Tujuan list, `-archonx` on every header, Indonesian, house
style).

### The C8 decision (user, 16 Oct)

The accepted Extended Abstract's Pendahuluan asserted a causal chain — a dropped fuel rod damaging
casings, ending in a leak — and attributed the emission to a specific element. The claim ledger records
that chain as **C8 = NOT FOUND** (no source) and records that **S2 supports only "ionizing radiation" in
general, not that element**. Against that, the admin's 14 Oct ruling froze Pendahuluan. The user decided
on 16 Oct:

> Keep the handling risk but strip the unsupported chain and the element attribution; re-source the dose
> and DNA claims from the ledger.

The draft does exactly that. **Kept:** the dose limits (20 mSv/yr workers, 50 mSv cap, 1 mSv/yr public,
0,6 mSv UNSCEAR average), the DNA-ionisation→cancer mechanism, remote handling as established practice
justified by dose reduction, the accuracy/handling background, and the core problem. **Removed:** the
unsourced mechanical-failure chain and the element attribution. The handling risk survives as a general
statement, not a sourced causal mechanism.

### Frozen-boundary compliance

Substance tokens checked present in both the accepted abstract's Pendahuluan and the draft: `dosis`,
`radiasi`, `20 mSv`, `DNA`, `kanker`, `reaktor`, `akurasi`, `operator`, `jarak`. The core-problem
sentence is carried unchanged, and the old comparison is demoted to motivation — "bukan lagi pertanyaan
penelitiannya … bagaimana bentuk perintah operator di dekat sasaran, bukan perangkat apa yang dipakai" —
so it never reads as a results section.

### Tujuan list (per ticket 04's PS2 amendment)

1. a 5-DOF teleoperated arm controlled by a PS2 controller;
2. the fine-positioning mode (gain reduction + release-to-hold);
3. its effect on placement error, 2-second hold success, and one-way latency at 1 m / 3 m under the
   2×2 protocol.

### Verification run (executed)

Word-boundary regex over the draft: `aplikasi web` 0 · `smartphone app` 0 · the two prohibited device
strings 0 · `joystick` 0 · the stripped element/chain terms 0. Citations resolve to existing ledger
entries only — **[1] = C1 + C2 (S2)**, **[2] = C3 (S1)**; no new ledger entry was needed. Every `#`
header ends `-archonx`.

Pre-edit backups: `.scratch/_backups/spc-full-paper-20261016-2204/` (this ticket, `map.md`,
`WORKFLOW-paper-development.md`).
