# Drafting loads — two-agent split-archonx

Written 16 Oct 2026. Splits the **9 remaining drafting tickets** between two agents working the same
effort, without two voices on the paper body and without two agents editing the same file.

Effort dir: `C:\Users\Arkandhafy\OneDrive\Documents\The Hivemind\Dingle's research\SPC Eureka 2026`.
Read `WORKFLOW-paper-development.md` and `map.md` first, then your load's tickets.

## The split

### Load A — paper body, one voice (owner: archonx01)

`12 Pendahuluan → 13 Metodologi → 14 Hasil dan Pembahasan → 15 Kesimpulan dan Saran → 16 Abstrak`

Sequential, each in a fresh context, grounded by `claim-ledger-archonx.md`. Reason for keeping these
together: they are one continuous argument, and the spec warns that parallel-drafting body sections
yields two voices.

### Load B — front/back matter + packaging (owner: archonx)

`17 Halaman Sampul → 19 Lampiran → 18 Daftar Pustaka → 20 Assemble, review, package`

Reason: fact-heavy, mechanical, and independent of the body prose — exactly the material the spec says
ports to parallel drafting. `18` can start from the claim ledger's source list immediately and take a
final numbering pass once Load A's sections land. `20` runs only after `16` (Load A) and `17`–`19`
(Load B) are actually `resolved`.

## Shared-file discipline (avoid clobbering)

- **Section drafts:** each load writes only its own `draft/NN-*.md` files. No cross-editing.
- **`map.md` and `claim-ledger-archonx.md`: Load A owns them.** Load B reads them; if it must record
  something, it appends it in its own ticket's `## Answer` and flags it for Load A to fold in. Reason:
  the ledger is the single grounding gate and two writers will collide.
- **`WORKFLOW-paper-development.md`:** Load A owns it (it carries the shared frontier).
- **GitHub mirror:** each load pushes its own branch `drafting/ticket-NN-<slug>` and opens a stacked PR
  on top of the current drafting head. No force-push. **Never merge** without the user's say-so.
- Each load backs up the files it will touch to `.scratch/_backups/spc-full-paper-<YYYYMMDD-HHMM>/`
  before editing.

## Convergence points

- `16 Abstrak` needs `12`–`15`; `20` needs `16`–`19`. Neither is started early — claimed only when every
  blocker is actually `resolved`, checked by reading the ticket files, not by assumption.

## Related

- **Hub:** [[Dingle's research/SPC Eureka 2026/SPC Eureka 2026 MOC|SPC Eureka 2026 MOC]]
- **Nearby:** [[Dingle's research/SPC Eureka 2026/WORKFLOW-paper-development|WORKFLOW-paper-development]], [[Dingle's research/SPC Eureka 2026/claim-ledger-archonx|claim-ledger-archonx]]
