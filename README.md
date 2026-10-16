# SPC Eureka 2026 — Wayfinder (Full Paper Repositioning)

Shared decision map for the SPC Eureka! ITB 2026 full paper (team deadline **18 Oct 2026**, official **23 Oct 2026**).

This repo is the **issue-tracker mirror** of a local wayfinder effort: the map and its decision
tickets live as markdown files, worked one ticket at a time until the way to the destination is
clear. The destination:

> A rewritten SPC full paper presenting a designed solution to the accuracy/handling problem —
> committed control paradigm (PS2-controller teleoperation), specified intervention (fine mode),
> and a locked 2×2 evaluation protocol — argued as design + explicitly-labelled expected results,
> since no physical data can be collected before submission.

## Layout

```
mindmap-rencana-konsep.png   ← visual mindmap of the whole concept plan (plain Indonesian)
rencana-konsep.md            ← the same concept plan as plain text (recommended read)
mindmap-rencana-konsep.svg   ← same, vector; .mmd = editable Mermaid source
map.md            ← the map: destination, notes, decisions-so-far, open items (START HERE)
spec.md           ← the full-paper spec synthesised from the closed map (9 mandatory sections,
                    locked decisions, evidence rules, pre-submission checks) — read after map.md
issues/           ← 01–07 = decision tickets (question + answer + comments history);
                    08–20 = drafting tickets (to-tickets breakdown: What to build / Blocked by)
adr/              ← architecture decision records (0001 camera autonomy, 0002 web joystick)
research/         ← research-ticket findings (guidebook, prior art, Blynk sourcing)
docs/             ← tracker conventions (issue-tracker.md) and domain notes
GLOSSARY.md       ← domain vocabulary (fine/coarse mode, condition A/B, pre-registered target, …)
claim-ledger-archonx.md ← the grounding gate: every external claim with its source and grade
AGENTS.md         ← agent entry points (tracker, domain docs, paper workflow)
WORKFLOW-paper-development.md ← the full chain map→spec→tickets→draft→review→submit
```

## Current status (16 Oct 2026)

- **7 of 7 wayfinder tickets resolved** — ticket 04 (paper restructure) closed **16 Oct 2026**.
- **Drafting stage started: tickets 08 and 09 are resolved.** 08 = root `GLOSSARY.md` (22 terms)
  plus domain-doc wiring. 09 = the sender-side ESP32 question is settled: it is **KEPT**, and ticket
  06's "sender ESP32 removed" cost saving is **retracted** (ticket 06 amendment 3; ADR 0002
  amendment 2).
- **Open: the paper title only.** The user confirmed on 16 Oct that the working title stays
  **TEMPORARY** and authorised the effort to proceed to the spec/drafting stage with it still
  provisional. It must be finalised before submission — see GitHub Issue #1 and the map's
  "Not yet specified".
- **Second open item — closed (ticket 09, 16 Oct):** the **sender-side ESP32 is retained**; it is
  the master MCU that reads the PS2 controller (PS2X library). The "sender ESP32 removed" cost claim
  is retracted and Feasibility now argues the 2-ESP32 design (the sender ESP32 is an already-owned
  part, so the interface change adds no MCU purchase). Committed chain: PS2 controller → sender
  ESP32 (PS2X) → Wi-Fi → receiver ESP32 → PCA9685 → MG996R servos.
- Control paradigm was amended twice this week: glove/IMU rejected (zero mentions), then
  phone-only digital control was superseded by the committed **PS2 controller** scheme
  (stick = multi-DOF rate control, ABXY = single joint, trigger = fine mode).
  Full rationale: ticket 06 amendments + `adr/0002-platform-esp32-hosted-web-joystick.md`
  (now a documented fallback) + `pitch-ps2-kontrol-archonx.md`.
- **Drafting ticket set published (08–20)** — the `to-tickets` stage: 13 slices (glossary
  prefactor, the two HITL decisions above, the nine mandatory sections, and assemble+review).
  Frontier right now: **10, 11, 12, 19** (11 was unblocked by 08; 10 still waits on the title).

## How to contribute to the open title decision

The title ticket is intentionally left open for team input. Two ways to weigh in:

1. **GitHub Issue (preferred):** open/comment on the issue labelled `title-decision` in this
   repo — proposals with reasoning.
2. **Direct edit:** edit `issues/04-paper-restructure.md` in a branch and open a PR against
   `main`.

Title rules established so far:
- Indonesian, follows the competition format (title edits were explicitly allowed by admin on
  14 Oct; Pendahuluan and the core problem stay locked).
- Must reflect the solution framing: PS2-controlled teleoperated 5-DOF arm + fine-positioning
  mode for radioactive-material handling accuracy.
- Watermark convention `-archonx` (the acting profile's name) applies to internal working titles
  and section headers.

## Conventions

See `docs/issue-tracker.md`: tickets carry `Type:` (research/prototype/grilling/task) and
`Status:` lines; blocking is a `Blocked by:` line; resolutions append under `## Answer`.
