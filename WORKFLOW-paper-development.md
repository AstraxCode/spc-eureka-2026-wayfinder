# Workflow: SPC Eureka 2026 full paper → submission-dingleberry

Reference card for developing the full paper from the wayfinder map through to submission.
Written 16 Oct 2026. Team deadline 18 Oct, official submission window 11–23 Oct 2026.

**Read the labels.** This doc mixes two different things:

- **[UPSTREAM]** — what the installed skills literally say (quoted, source named).
- **[INFERRED]** — my mapping of that flow onto a *paper*. The skills were written for code, so
  this mapping is judgement, not documentation. Where it matters, it says so.

Nothing here is a decision. The decisions live in the wayfinder map and its tickets.

---

## TL;DR — the chain

```
wayfinder  →  to-spec  →  to-tickets  →  implement  →  code-review  →  pr  →  retro
   ✅done      ✅done      ✅PR#2        ⬜          ⬜             ⬜      ⬜
                            │
                            └── drafting engine: writing-fragments → writing-shape
                                grounding gate:   grounded-citations + claim-ledger
                                domain overlay:   paper-architecture
```

**[UPSTREAM]** `ask-matt` states the handoff rule for exactly this situation:

> When the map clears, **it hands off, it doesn't build**: merge onto the main flow at
> **`/to-spec`**, which collapses the map's linked decisions into a buildable plan, then
> `/to-tickets` and `/implement` as usual. Looping the map straight into `/implement` skips that
> collapse and throws the linked detail away, so go straight to `/implement` only when the effort
> turned out genuinely small.

So: never jump from the map straight to writing the paper.

---

## Where things live

| Thing | Path |
|---|---|
| Effort dir | `C:\Users\Arkandhafy\OneDrive\Documents\Claude's brain\Dingle's research\SPC Eureka 2026` |
| Wayfinder map | `.scratch/spc-full-paper/map.md` |
| Spec | `.scratch/spc-full-paper/spec.md` |
| Tickets | `.scratch/spc-full-paper/issues/01..07-*.md` |
| ADRs | `.scratch/spc-full-paper/adr/0001-*.md`, `0002-*.md` |
| Research findings | `.scratch/spc-full-paper/research/` |
| Claim ledger (grounding gate) | `claim-ledger-dingleberry.md` |
| Glossary (domain vocabulary) | `GLOSSARY.md` |
| Paper template | `Full paper/Format Full Paper.docx` |
| Tracker conventions | `docs/agents/issue-tracker.md` |
| Pre-edit backups | `.scratch/_backups/` |
| GitHub mirror | https://github.com/AstraxCode/spc-eureka-2026-wayfinder (private) |
| Mirror staging clone | `%LOCALAPPDATA%\hermes\profiles\archonx\cache\scratch\spc-wayfinder-repo` |
| Open title decision | GitHub Issue #1 |

---

## Current state (verified 16 Oct 2026, 16:45)

- All **7 of 7** wayfinder tickets `Status: resolved`. Ticket 04 (paper restructure) closed today,
  with the 15 Oct PS2 pivot recorded in it and in both ADRs.
- `spec.md` written — the collapsed decisions (9 mandatory sections, equations, evidence rules,
  9 pre-submission checks).
- **`to-tickets` done (16 Oct):** 13 drafting tickets `issues/08..20` published (glossary prefactor;
  the two HITL decisions — sender-ESP32 and title; the nine mandatory sections; assemble+review).
  Blocking edges wired as text; frontier = **08, 09, 10, 12, 19**. On branch
  `to-tickets/paper-draft-2026-10-16`, **PR #2 open** (not merged — user decides).
- `map.md` is still **`Status: open`**: the title is the one decision not made. That is deliberate —
  the map is not done while a decision is open, even though the effort is authorised to proceed.
- GitHub mirror synced, `HEAD == origin/main` at `e596a50`. Issue #1 open, 1 comment.
- Backups: `.scratch/_backups/spc-full-paper-20261016-1640/` (pre-ticket-04-close).

---

## The workflow, stage by stage

### Stage 0 — the map closes **[UPSTREAM: `wayfinder`]**

Wayfinder produces decisions, not deliverables. It hands off. Done.

### Stage 1 — collapse the decisions into a plan **[UPSTREAM: `to-spec`]**

`to-spec` turns the conversation into a spec and publishes it to the tracker — no interview, pure
synthesis. **Done**: `.scratch/spc-full-paper/spec.md`.

**[INFERRED]** `to-spec`'s template is software-shaped (seams, modules, testing decisions). It was
adapted: "Implementation Decisions" became the locked paper decisions, "Testing Decisions" became
the pre-submission compliance/grounding audit plus the promised 2×2 protocol, and "seams" became
the rubric rows and the claim ledger.

### Stage 2 — break the plan into tickets **[UPSTREAM: `to-tickets`]** ✅ done (13 tickets, PR #2 open)

`to-tickets` breaks the plan into **tracer-bullet vertical slices**, each sized to one fresh context
window, each declaring its **blocking edges** (the tickets that must finish first). It then
**quizzes you on the breakdown** — granularity, blocking correctness, merge/split — and only
publishes after you approve.

**[INFERRED]** A paper has no layers, so a "vertical slice" becomes a **section**, and the blocking
edges are real: an abstract cannot be drafted before the sections it summarises exist.

Proposed breakdown (to be quizzed and approved before anything is published):

| Ticket | Blocked by | Delivers |
|---|---|---|
| `Dasar Teori` | — | Theory base the intervention leans on |
| `Pendahuluan` | — | Locked background, verbatim in substance |
| `Metodologi` | `Dasar Teori`, **sender-ESP32 decision** | Architecture + intervention + 2×2 plan |
| `Hasil dan Pembahasan` | `Metodologi` | Expectations analysis + targets table + limits |
| `Kesimpulan dan Saran` | `Hasil dan Pembahasan` | Contribution + limits + camera future work |
| `Abstrak` | every section above | The summary, written last |
| `Halaman Sampul` | **title decision** | Cover page |
| `Daftar Pustaka` | all citing sections | Bibliography from the claim ledger |
| `Lampiran` | — | Wiring / component appendices |

**[INFERRED] The "wide refactor" exception applies to one thing.** `to-tickets` carves out
mechanical changes whose blast radius fans across everything (rename a column → thousands of call
sites) and sequences them **expand → contract**. The title and the `-dingleberry` watermark header
convention are exactly that shape: they touch every header. Sequence them expand–contract — keep the
title in **one place** now, substitute once at the very end. Already built into `spec.md`.

### Stage 3 — draft **[UPSTREAM: `implement` / `implement-spec`]**

`implement` takes a spec or ticket and does the work; it calls `tdd` at pre-agreed seams, checks
regularly, then calls `code-review`, then commits. `implement-spec` reads the tickets as a task
graph and runs implementer subagents across the ready **frontier** in parallel, landing everything
on one integration branch.

**[INFERRED]** Use `implement` per section. `implement-spec`'s parallelism does port, but only for
genuinely independent, fact-heavy sections (`Lampiran`, `Daftar Pustaka`) — parallel-drafting
`Dasar Teori` and `Metodologi` yields two voices.

### Stage 3a — the actual writing engine **[UPSTREAM: `writing-fragments`, `writing-shape`, `writing-beats`]**

These are the prose skills, and they are **beta** (`in-progress/`, excluded from the upstream plugin,
no docs pages, "can change or disappear without warning").

- `writing-fragments` — pure **explore**: a grilling session that mines fragments into one markdown
  file, no structure imposed. **Your pile already exists**: ticket answers, ADRs, `research/*.md`,
  `rencana-konsep.md`, the pitch doc. No new session needed — point it at that material.
- `writing-shape` — **exploit**: read the pile end-to-end, commit to a structure, mine the pile to
  fill it paragraph by paragraph, arguing format choices at each step. **Use this one.** The
  structure is externally imposed by the guidebook, so there is nothing to choose.
- `writing-beats` — the alternative: choose-your-own-adventure beats, grounding each term before a
  beat leans on it. Better for narrative than for a mandated 9-section paper. Skip.

### Stage 3b — what replaces `tdd` **[INFERRED]**

`tdd` is red-green-refactor on tests. A paper has no test suite, so the feedback loop has to come
from somewhere else:

**`grounded-citations` + `claim-ledger-dingleberry.md` are the red test.** A claim with no source
is red. You make it green by sourcing it *or* labelling it an explicitly pre-registered expectation.
Never a third option. This is the single most important substitution in this doc — it is what keeps
the disqualification risk (guidebook p. 5 item 7, fabrication) at zero.

### Stage 3c — the domain overlay **[your skill: `paper-architecture`]**

Concept-build first, then write: read local notes for gaps, source the missing foundations into
`RnD Scraping/`, then every technical claim carries a verified link. It also sets the house style
(blunt/direct) and the `-dingleberry` watermark rule, and warns that **claims must match the
decision records including later amendments** — drafting from a superseded ticket silently
reintroduces a rejected design. That warning already bit once (the PS2 pivot went unrecorded in
ticket 04 for a day).

`to-questionnaire` handles the blockers that live in someone else's head rather than in the docs:
the *built-prototype* question, and the real PS2 listing.

### Stage 4 — review **[UPSTREAM: `code-review`]**

`code-review` runs a **two-axis** review of a diff against a fixed point, as **parallel sub-agents**
so the two contexts don't pollute each other: **Standards** (does it follow this repo's documented
standards?) and **Spec** (does it match the originating issue/spec?).

**[INFERRED]** The shape ports wholesale; only the sources change:

| `code-review` axis | Paper equivalent |
|---|---|
| Standards | Guidebook format/structure rules + the 9-section checklist + `paper-architecture` house style |
| Spec | `.scratch/spc-full-paper/spec.md` |
| Smell baseline (Fowler ch.3) | **Does not transfer.** Paper equivalent: an unsourced number, an expectation phrased as a result, a term used before it's defined, a header missing its watermark, a claim contradicting a superseded ticket answer |

Keep the mechanism: labelled heuristics, repo-documented rules override the baseline, run the two
sub-agents in parallel. `grilling` is also worth a round here against the rubric rows.

### Stage 5 — package for submission **[UPSTREAM: `pr`, repurposed]**

`pr` exists to shape a change into something a reviewer accepts: the smallest visual, before/after
evidence, a one-way-or-two-way-door call.

**[INFERRED]** For a paper that is the submission package: cover page, `docx` into the official
template, `pdf` export, correct filename `SPC_FullPaper_NamaKetuaTim.pdf`, upload via eurekaitb.com
before 23 Oct. `handoff` if a teammate takes a section over; `github-repo-management` to re-sync the
mirror so the team never reads a superseded decision.

### Stage 6 — close the loop **[UPSTREAM: `retro`]**

`retro` looks back over a session and proposes changes to the **agent's environment**, not the work:
navigation pointers, automated checks, standards, tooling. Mechanical mistakes become deterministic
checks; judgement calls become standards.

**[INFERRED]** Run it after submission, then start `wayfinder` again for the Final stage
(28–29 Nov) — the 2×2 experiment is a new, larger effort and deserves its own map.

---

## Do not use

`tdd`, `codebase-design`, `diagnosing-bugs`, `triage`, `improve-codebase-architecture`,
`setup-pre-commit`, `migrate-to-shoehorn`, `scaffold-exercises`, `git-guardrails-claude-code` —
nothing to test, triage, refactor, or hook.

`to-spec` is **already spent** on this effort (spec.md exists). Re-running it would overwrite the
collapse you already have.

---

## Context hygiene **[UPSTREAM: `ask-matt` → Phase boundaries]**

- Keep **grilling → spec → tickets in one unbroken context window**, so they build on the same
  thinking. Each `implement` then starts fresh, working from its ticket.
- At a **phase boundary** the five options are: **Continue** / **clear** / **handoff** / **subagent**
  / **compact**. `/compact` is the default — the bottom of the tree, not the first reach. `handoff`
  is narrow: only a new harness, a new directory, a colleague, or forking a mid-phase side task.
- Watch the **smart zone** (~150k tokens). If a session approaches it before `to-tickets`, don't push
  on degraded — compact at the nearest boundary.

---

## Blockers (both already in the map + spec)

1. **The title.** Provisional. Blocks `Halaman Sampul`. Live as GitHub Issue #1, open on purpose so
   a teammate can propose.
2. **Sender-side ESP32, kept or removed.** Ticket 06 amendment 2 lists it as a *pending
   re-decision* and nobody re-decided it. A PS2 controller needs a master MCU to read it (PS2X
   library), so ticket 06's original "sender ESP32 removed" cost saving cannot stand as written —
   and Feasibility is 15% of the rubric. The pitch doc implies the sender is **kept**. Blocks
   `Metodologi` and the cost sentence.

Also unresolved, for the team: **does the arm physically exist as a built prototype?** No photos, no
firmware, no STL anywhere in this tree, yet the Extended Abstract states build steps in past tense.
`Hasil dan Pembahasan` wording depends on the answer.

And the price: **Rp40k–70k is a team estimate**, not a verified listing. It may enter the paper only
carrying that label, or after a real listing link is captured.

---

## Environment fixes worth doing

- ~~`AGENTS.md` declares a root `GLOSSARY.md` and `docs/adr/`. **Neither exists**~~ — **DONE 16 Oct
  (ticket 08).** Root `GLOSSARY.md` now exists (22 terms); `AGENTS.md` and `docs/agents/domain.md`
  now point at `.scratch/spc-full-paper/adr/`, where the ADRs actually live.
- Record amendments **immediately, mid-interview**, in the ORIGINAL ticket. The PS2 pivot sat
  unrecorded in ticket 04 for a day and left four stale artifacts behind it.
- Keep `ANTHROPIC`/GitHub tokens out of these docs. `gh` is authenticated as `AstraxCode` via
  keyring; never echo or export the token.

---

## How to resume

1. Read `.scratch/spc-full-paper/map.md` first — the low-res view of every decision.
2. Read `.scratch/spc-full-paper/spec.md` for the collapsed plan.
3. `to-tickets` **done** — 13 tickets `issues/08..20` published (PR #2, awaiting merge). Work the
   frontier (09, 10, 12, 19 — 08 resolved 16 Oct) blockers-first.
4. Work tickets blockers-first with `implement`, each in a fresh context, grounded by the claim
   ledger.
5. Re-sync the GitHub mirror after every session that edits the tracker.

**Upstream source:** `mattpocock/skills` v1.3.1 @ `49dd158`, archived at
`AI bank/Skills Library/imported skills/mattpocock-skills`; installed into the Hermes `archonx`
profile on 16 Oct 2026.
