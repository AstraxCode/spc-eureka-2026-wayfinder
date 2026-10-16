---
Type: grilling
Status: resolved
Blocked by: 02
---

## Question

Lock the experiment protocol that will prove the intervention works:

- Conditions: baseline vs intervention on the chosen controller — confirm A/B, and whether
  distance (1 m / 3 m) stays a variable or is fixed.
- Trial count per condition FOR THE NEXT STAGE (no trials are possible before 18 Oct — the
  prototype is locked behind this submission). The paper presents the protocol as a plan, with
  expected results labelled as expectations.
- Operators: how many, whether each runs both conditions, and how operator variation is handled
  (paired design vs separate pools).
- Randomisation/order (was the original 40-trial protocol counterbalanced?) and the exact
  success criterion for the 2-second hold.
- Placement-error measurement method on the grid, and how latency is timestamped given the
  one-way t_receive - t_send formula already in the paper.
- What must be held constant (object, gripper force, Wi-Fi channel, target zone) — carried over
  from the original methodology.

## Answer

**Locked protocol (settled with the user 14 Oct; next-stage plan, presented in the paper with
expected results explicitly labelled):**

1. **Design: 2×2** — condition (A: baseline app control vs B: fine mode — gain reduction +
   release-to-hold latch) × distance (1 m, 3 m). Distance stays a variable; it carries the
   latency-vs-distance physics claim (claim ledger C5/C6).
2. **Trials: 40 per operator per condition**, exactly as the submitted abstract states. Pass
   criterion for the 2-second hold: **8 of 10 trials on-target** (abstract's threshold, unchanged).
3. **Operators: 3, paired** (each operator runs all four cells) — **fallback to 2 operators if
   circumstances force it** (documented contingency, not silent change). 3 ops × 4 cells × 40
   trials = 480 trials planned.
4. **Order: counterbalanced** — operators alternate which condition runs first, to preempt
   learning-effect objections (new vs the abstract, which specified no ordering).
5. **Placement error:** distance from object centre to target centre on the marked grid, measured
   by phone photo against grid markings (unchanged from the abstract).
6. **Held constant (carried from the abstract):** foam object, operator, Wi-Fi environment, target
   zone. Platform per ADR 0002: ESP32-hosted web joystick for both conditions; latency measured
   one-way (t_receive − t_send) and pre-registered as in-team targets per the ticket-07 rule.
