---
Type: research
Status: resolved
Blocked by:
---

## Question

Ground the intervention in published work so the paper is not an unsupported invention. Find
primary sources (IEEE, MDPI, arXiv, journal papers) on:

1. Input filtering / smoothing of operator commands in teleoperated manipulators, and its measured
   effect on task accuracy.
2. Fine-positioning strategies: gain/scale reduction near a target, rate control vs position
   control, clutch or rebinding behaviour in master-slave systems.
3. The accuracy-vs-latency tradeoff introduced by filtering remote-control commands.
4. Which metrics the literature uses for telemanipulation handling/accuracy (e.g. target
   acquisition error, time-on-target, throughput) — so our three metrics can be aligned or
   contrasted with standard ones.

Write findings to `.scratch/spc-full-paper/research/05-prior-art.md`, every claim carrying its
source URL, and flag anything you could not source rather than filling the gap.

## Answer

Full findings: `../research/05-prior-art.md` (13 sources logged, 5 core sources with URLs). Key results:

1. **Smoothing**: 2024 IEEE filter-comparison study supports reduction of input oscillation (Savitzky–Golay 26.74% smoother trajectories) but reports NO task-placement-accuracy result. **No direct evidence found that command smoothing alone improves placement accuracy** — treat smoothing as a hypothesis, not a proven intervention.
2. **Fine positioning**: strong support for adaptive/variable motion scaling and position/rate hybrid control — Richter 2019 (ICRA): lower error rates under delay with 17 participants; Han & Yang 2022 (Applied Sciences, nuclear-fuel-handling task): hybrid position–rate control −17.23% completion time, −34.02% NASA-TLX; Lee 2024 (Springer, abstract-only): variable scaling −20.2% time, −36.6% NASA-TLX.
3. **Latency**: literature establishes a delay↔accuracy tension but NO numeric accuracy-vs-filter-latency curve; report network one-way latency and local filter delay separately.
4. **Metrics**: standard measures are placement error/completion time/error rate/clutch count/NASA-TLX. The 2-second hold is a project-defined criterion (do not label it standard); Fitts-throughput not established as standard here.
5. **Gaps flagged honestly**: no IMU+flex-sensor smoothing test in literature; Springer source abstract-only (paywalled), confidence capped.
