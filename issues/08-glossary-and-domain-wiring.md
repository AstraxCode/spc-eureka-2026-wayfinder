# 08: GLOSSARY + domain-doc wiring

**What to build:** A single root `GLOSSARY.md` defining the paper's domain vocabulary so every
drafting ticket speaks one language, and point the repo's domain-doc declarations at the ADRs
where they actually live. Fixes the `AGENTS.md` drift (it declares a root `GLOSSARY.md` and
`docs/adr/` that do not exist; the ADRs live under `.scratch/spc-full-paper/adr/`).

**Blocked by:** None (can start immediately).

**Status:** ready-for-agent

- [ ] `GLOSSARY.md` exists at the effort root with entries for: teleoperation, fine mode, coarse
      mode, condition A, condition B, release-to-hold, gain reduction, pre-registered target,
      grid cell, 2-second hold, open-loop, PS2 controller.
- [ ] Every definition is consistent with `map.md` / `issues/` / `spec.md` and contradicts no ADR
      (0001 rejected camera autonomy; 0002 web-joystick fallback).
- [ ] `AGENTS.md` "Domain docs" section points at the real ADR directory.
- [ ] No stale interface wording ("aplikasi web" / "smartphone app") appears in any definition.
