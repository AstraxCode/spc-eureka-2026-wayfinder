# 08: GLOSSARY + domain-doc wiring

**What to build:** A single root `GLOSSARY.md` defining the paper's domain vocabulary so every
drafting ticket speaks one language, and point the repo's domain-doc declarations at the ADRs
where they actually live. Fixes the `AGENTS.md` drift (it declares a root `GLOSSARY.md` and
`docs/adr/` that do not exist; the ADRs live under `.scratch/spc-full-paper/adr/`).

**Blocked by:** None (can start immediately).

**Status:** resolved

- [x] `GLOSSARY.md` exists at the effort root with entries for: teleoperation, fine mode, coarse
      mode, condition A, condition B, release-to-hold, gain reduction, pre-registered target,
      grid cell, 2-second hold, open-loop, PS2 controller.
- [x] Every definition is consistent with `map.md` / `issues/` / `spec.md` and contradicts no ADR
      (0001 rejected camera autonomy; 0002 web-joystick fallback).
- [x] `AGENTS.md` "Domain docs" section points at the real ADR directory.
- [x] No stale interface wording ("aplikasi web" / "smartphone app") appears in any definition.

## Answer

**Resolved 2026-10-16 (ArchonX).** `GLOSSARY.md` created at the effort root — 19 terms in four
groups (control paradigm, control chain, evaluation, working conventions), format per the
`domain-modeling` skill: opinionated, one-to-two-sentence definitions, `_Avoid_` synonyms.

The 12 required terms are all present, plus 7 the drafting tickets would otherwise re-invent:
**Stick**, **fallback**, **operator**, **placement error**, **one-way latency**, **expected
result**, **team estimate**. Each of those is load-bearing in a specific ticket: `Stick` for
ticket 13's architecture, `fallback` for the ADR-0002 demotion, `operator` and `placement error`
for ticket 13's protocol, `one-way latency` for the latency definition, `expected result` and
`team estimate` for ticket 14's labelling discipline.

Deliberate choices worth flagging:

1. **`Fine mode` explicitly excludes "smoothing"/"filtering" and "clutch".** The intervention is a
   gain reduction, not a filter; the literature's hardware clutch is what release-to-hold
   replaces. Conflating them would import the unsupported claim that smoothing improves accuracy
   (prior-art finding 1).
2. **`2-second hold` carries "project-defined" inside the definition**, so a drafting agent cannot
   cite it as a standard metric without contradicting the glossary (spec Testing Decision 8).
3. **`sender-side ESP32` is recorded as OPEN, not settled.** The definition states the retention
   question is undecided and that the paper must not describe either state before ticket 09. The
   glossary therefore does not pre-empt ticket 09.
4. **`Pre-registered target` and `team estimate` are defined as evidence statuses**, not values,
   so the two unverified items (≤ 200 ms; Rp40k–70k) can be written down without becoming claims.
5. **No prohibited interface string appears at all** — the `PS2 controller` entry points at
   `spec.md` Testing Decision 7 for the list instead of spelling the strings out, so even the
   glossary's own `_Avoid_` lines stay clean for the ticket-20 forbidden-content grep.

**Domain-doc wiring fixed.** `AGENTS.md` "Domain docs" now names the real ADR location
(`.scratch/spc-full-paper/adr/`, not the non-existent `docs/adr/`), and `docs/agents/domain.md`
gained a "This repo's paths" section that overrides its generic layout for this repo — otherwise
the skill's own instructions would keep sending readers to `docs/adr/`.

**Verification run:** all 12 required terms present; zero hits for "aplikasi web" / "smartphone
app"; no camera-autonomy plan asserted (ADR 0001); web joystick appears only as the documented
fallback (ADR 0002); sender-ESP32 left open (ticket 09); only two numbers in the whole file
(200 ms, 8 of 10), both carried from the claim ledger and the locked protocol.

Pre-edit backups: `.scratch/_backups/spc-full-paper-20261016-1956/` (AGENTS.md, domain.md, this
ticket).

