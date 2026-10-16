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
map.md            ← the map: destination, notes, decisions-so-far, open items (START HERE)
issues/           ← one file per decision ticket (question + answer + comments history)
adr/              ← architecture decision records (0001 camera autonomy, 0002 web joystick)
research/         ← research-ticket findings (guidebook, prior art, Blynk sourcing)
docs/             ← tracker conventions (issue-tracker.md) and domain notes
```

## Current status (16 Oct 2026)

- **6 of 7 tickets resolved.**
- **Open: the paper title** — the only remaining decision. See ticket 04
  (`issues/04-paper-restructure.md`) and the map's "Not yet specified".
- Control paradigm was amended twice this week: glove/IMU rejected (zero mentions), then
  phone-only digital control was superseded by the committed **PS2 controller** scheme
  (stick = multi-DOF rate control, ABXY = single joint, trigger = fine mode).
  Full rationale: ticket 06 amendments + `adr/0002-platform-esp32-hosted-web-joystick.md`
  (now a documented fallback) + `pitch-ps2-kontrol-dingleberry.md`.

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
- Watermark convention `-dingleberry` applies to internal working titles and section headers.

## Conventions

See `docs/issue-tracker.md`: tickets carry `Type:` (research/prototype/grilling/task) and
`Status:` lines; blocking is a `Blocked by:` line; resolutions append under `## Answer`.
