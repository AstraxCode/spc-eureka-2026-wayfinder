# Spec: SPC Eureka 2026 full paper — solution-framed repositioning-dingleberry

Status: ready-for-agent
Effort: `.scratch/spc-full-paper/` (wayfinder map: all 7 tickets resolved 16 Oct 2026)
Date: 16 Oct 2026 — team deadline 18 Oct 2026, official submission window 11–23 Oct 2026
Source of truth: `map.md`, `issues/*.md`, `adr/*.md`, `research/*.md`, `claim-ledger-dingleberry.md`

> This spec synthesises the decisions already settled in the wayfinder map and its tickets. It
> introduces no new decisions. One item is deliberately left open and is marked **OPEN** below.

## Problem Statement

The team's accepted Extended Abstract framed the work as a **comparison** (web/app control vs a
glove/IMU input) and the full paper inherits that framing, plus a stale control interface.

The team now has to produce a full paper that:

- reads as **a designed solution to a problem**, not a survey or a comparison, because the rubric
  scores *Inovasi dan Orisinalitas* (20%) and *Metodologi* (20%) and the "must solve a problem"
  criterion is a hard rule (guidebook p. 5 item 5) — while noting that the guidebook never states a
  comparison-only penalty, so none may be inferred;
- reports **no new empirical results**, because the prototype is locked behind the full-paper stage
  and zero trials are possible before 18 Oct 2026 (hard constraint, established 13 Oct);
- keeps the **radiation/accuracy-and-handling background intact** in substance and keeps
  **Pendahuluan and the core problem frozen** (admin ruling 14 Oct — the one hard boundary);
- describes the control interface as a **PS2 controller**, not a smartphone/web app, because the
  input device was pivoted on 15 Oct; and
- does not fabricate data, which the guidebook punishes with disqualification (p. 5 item 7).

## Solution

A 10–20 page Indonesian full paper (excluding cover, bibliography, appendices) that presents the
work as **design + explicitly-labelled expected results**. The contribution is stated as an
**operator-side fine-positioning intervention**: a PS2-controller teleoperation scheme with a
trigger-toggled fine mode (reduced command-to-joint gain) plus a release-to-hold behaviour, argued
against established motion-scaling / hybrid position-rate control prior art, and validated by a
locked 2×2 protocol that the team will run in the next stage.

Metrics are retained and unchanged: **placement error**, **2-second hold success**, **one-way
latency** (all three presume human teleoperation, which the PS2 pivot preserves).

## User Stories

1. As **a competition judge (penilai)**, I want the paper to open with a clearly stated problem it
   solves, so that I can score *Inovasi dan Orisinalitas* without having to infer the contribution.
2. As **a competition judge**, I want a single committed control paradigm, so that I am not asked to
   weigh two half-argued alternatives.
3. As **a competition judge**, I want the Metodologi to describe an implementable design, so that I
   can score *Metodologi* on the method rather than on promises.
4. As **a competition judge**, I want every result-shaped number labelled as an expectation, so that
   I can trust the paper's integrity.
5. As **a competition judge**, I want the paper to acknowledge what it does *not* show, so that the
   limits are honest rather than concealed.
6. As **a competition judge**, I want claims traceable to cited sources, so that *Dasar Teori* and
   *Sistematika Penulisan* can be scored on the referenced literature.
7. As **the team**, I want the Pendahuluan and core problem left untouched, so that we comply with
   the admin's 14 Oct ruling and keep Extended-Abstract continuity.
8. As **the team**, I want the paper to keep the three established metrics, so that the evaluation
   the team already planned still validates the stated contribution.
9. As **the team**, I want the 2×2 protocol described exactly as it will be executed, so that the
   Final stage runs the protocol the paper promised.
10. As **the team**, I want the equations consistent with the described pipeline, so that reviewers
    can follow the mapping from operator input to joint command.
11. As **the team**, I want the PS2 controller described as the committed device with the web
    joystick as a documented fallback, so that the disclosure matches what we will actually build.
12. As **the team**, I want the controller's price to carry its evidence status, so that the
    Feasibility argument (15%) is defensible and no unverified figure is stated as fact.
13. As **the team**, I want the glove/IMU and analog-joystick options absent from the paper, so that
    the submission does not re-open a path the team explicitly rejected.
14. As **the team**, I want the camera-autonomy rejection carried as one future-work paragraph, so
    that the rejected path is on record without becoming a second plan.
15. As **an operator** running the Final stage, I want the fine-mode mechanism fully specified
    (trigger toggle, gain reduction, release-to-hold), so that I can run both conditions without
    making design decisions mid-test.
16. As **an operator**, I want the release-to-hold behaviour explained in the paper, so that my
    natural "centre the stick" action is understood as the intended hold mechanism.
17. As **an operator**, I want the trial protocol (condition × distance, trials, success criterion)
    fixed in advance, so that my runs are pre-registered and not adjusted after the fact.
18. As **a technical reader**, I want the control chain drawn end to end (controller → MCU → Wi-Fi →
    receiver → servo driver → servos), so that the latency claim has a visible physical origin.
19. As **a technical reader**, I want motion scaling and hybrid position/rate control cited as prior
    art, so that the scheme reads as a grounded application rather than an invention.
20. As **a technical reader**, I want the limits of this work stated plainly (tabletop proof of
    concept; not a claim about real fuel-rod handling), so that I do not over-read the results.
21. As **a technical reader**, I want to know the receiver stays open-loop with no new sensors, so
    that I understand where the precision comes from.
22. As **the competition admin (panitia)**, I want the formatting rules followed (PDF, Bahasa
    Indonesia, Times New Roman 12 pt, 1.15 spacing, A4, 2.54 cm margins, 10–20 pages, prescribed
    filename), so that the paper passes the format check and is graded at all.
23. As **the competition admin**, I want all nine mandatory sections present, so that the paper is
    structurally compliant.
24. As **the team lead**, I want the reference list complete and every citation real, so that the
    academic-integrity rule is not breached.
25. As **the team lead**, I want every external claim tied to a source in the claim ledger, so that
    drafting does not invent numbers under deadline pressure.
26. As **the team lead**, I want an internal title placeholder that is clearly marked provisional,
    so that the paper can be drafted before the title is finalised.
27. As **the team lead**, I want the final title to be swappable in one place, so that the late
    title decision doesn't force a rewrite.
28. As **the team lead**, I want the paper to fit 10–20 pages, so that no required section is cut
    for length.
29. As **a Final-stage committee member**, I want the expected-results targets to be numeric and
    pre-registered, so that I can compare the actual results against a claim made in advance.
30. As **a Final-stage committee member**, I want to see which parts were deliberately deferred
    (measured latency figures), so that absence of data is distinguishable from omission of data.

## Implementation Decisions

### Mandatory structure (guidebook p. 15 — all nine required, in this order)

1. Halaman Sampul
2. Abstrak
3. Pendahuluan
4. Dasar Teori
5. Metodologi
6. Hasil dan Pembahasan
7. Kesimpulan dan Saran
8. Daftar Pustaka
9. Lampiran

### Section-by-section content

- **Abstrak** — reframed to the solution: the contribution is the fine-positioning intervention; the
  2×2 protocol is presented as planned validation; every result-shaped statement is labelled an
  expectation. No "aplikasi web" wording.
- **Pendahuluan** — the accuracy/handling background for radioactive-material handling, retained in
  substance and **not restructured** (admin ruling). The old comparison appears here only as
  motivation for why a control-side intervention is the gap being addressed.
- **Dasar Teori** — rebuilt on **motion scaling** and **hybrid position/rate control** prior art
  (Richter 2019; Han & Yang 2022; Lee 2024), plus the filtering literature, with the honest note
  that no direct evidence was found that command smoothing alone improves placement accuracy —
  smoothing is presented as a hypothesis, not a proven effect.
- **Metodologi** — three parts: (i) the control architecture, (ii) the intervention specification,
  (iii) the 2×2 validation protocol as a plan.
- **Hasil dan Pembahasan** — an expectations-analysis section: explicit labelling statement at the
  top, a pre-registered-targets table, the expected-outcome analysis, and an **honest-limits
  subsection**. It does not report measured data, because none exists.
- **Kesimpulan dan Saran** — restates the contribution and the limits; carries the camera-autonomy
  future-work paragraph (from ADR 0001).
- **Daftar Pustaka / Lampiran** — bibliography from the claim ledger's sourced entries; appendices
  for the circuit/wiring and component material.

### Control interface and architecture

- Committed input device: **PS2 controller** — analog stick = coordinated multi-DOF rate control
  (stick forward → end-effector forward); **ABXY** = select a single joint, then the stick drives
  only that joint; **trigger** = fine-mode toggle, an **independent mechanism** from the stick and
  buttons (Q9(i), approved).
- The ESP32-hosted web joystick (ADR 0002) is a **documented fallback**, not the described primary
  interface. Blynk Cloud remains the fallback chain behind it.
- Glove/IMU and any analog physical joystick: **zero mentions** anywhere in the paper.
- Receiver side unchanged: **open-loop**, no encoders, no new sensors, PCA9685 + MG996R servos;
  precision comes from the operator-side mode plus firmware limits.
- **Resolved 16 Oct (ticket 06 amendment 3; ADR 0002 amendment):** the sender is a **commodity
  operator-side laptop** — PS2 controller → PS2-to-USB adapter → laptop → Wi-Fi (**UDP**) →
  receiver ESP32 → PCA9685 → servos. No bespoke sender MCU; the original "sender ESP32 removed"
  cost claim stands. The OS/host hop is the disclosed latency-jitter source (mitigations: UDP,
  dedicated link, power-save off, raw HID, fixed-rate loop). One-way latency remains a
  pre-registered target (≤ 200 ms), never a measured result.

### Intervention specification

Fine mode = **gain reduction near the target** + **release-to-hold** behaviour. Under stick rate
control, release-to-hold is inherent: stick centred = zero command velocity = arm holds. The paper
frames the software latch as a design contribution replacing the literature's hardware clutch.

### Equations

- eq (2) — kept, relabelled as the **baseline coarse mapping** (device-agnostic).
- **new fine-mode equation** — added; expresses the gain reduction. Device-agnostic.
- eqs (1), (3) — torque / latency, retained.
- eqs (4)–(6) — statistics, retained unchanged.
- No equation may reference a web/app UI.

### Evidence rules (binding on drafting)

- Every external claim carries a source; the claim ledger (`claim-ledger-dingleberry.md`) is the
  gate. Nothing enters the paper that the ledger does not carry.
- **Pre-registered targets only**: one-way latency ≤ 200 ms (already in the ledger as a
  pre-registered target) and placement error within one grid cell — the numeric grid value is
  derived at draft time from the actual grid spacing, never invented.
- Never present an expectation as a result. Never fabricate a citation or a value.
- The 2-second hold criterion is **project-defined** — it must not be labelled a standard metric.
- Controller price: **team estimate Rp40k–70k**, and it may enter the paper only carrying that
  team-estimate label, or after a real listing link is captured. This is the only external fact
  currently in the ledger without a live source.
- Label anything pending into the Final stage as expected, not measured.

### Formatting and conventions

- PDF, Bahasa Indonesia, Times New Roman 12 pt, 1.15 spacing, A4, 2.54 cm margins, 10–20 pages
  excluding cover/bibliography/appendices; filename `SPC_FullPaper_NamaKetuaTim.pdf`.
- Template authority: `Full paper/Format Full Paper.docx`.
- Watermark `-dingleberry` on the title and section headers (internal working convention).

## Testing Decisions

Because the deliverable is a document, "testing" is the set of checks that the paper is compliant,
grounded and honest — plus the validation protocol the paper promises.

### What makes a good check here

A check must be **verifiable from the artefact itself or from a cited source** — never from the
author's confidence. Checks test external behaviour (does the paper claim only what it can support?)
rather than drafting style.

### Checks to run before submission

1. **Section completeness** — all nine mandatory sections present, in order.
2. **Format compliance** — the guidebook's mechanical rules (language, font, spacing, margins, page
   count, filename), because the format check gates grading entirely.
3. **Rubric self-review** — score the draft against the Full Paper rubric rows (Analisis dan
   Pembahasan 25%, Metodologi 20%, Inovasi dan Orisinalitas 20%, Feasibility 15%, Dasar Teori 10%,
   Sistematika Penulisan 10%) and state where each is weak.
4. **Claim-ledger coverage audit** — every number and external assertion in the draft maps to a
   ledger entry with a source; anything unmapped is deleted or sourced.
5. **Expectation-label audit** — grep the draft for result-shaped statements and confirm each is
   labelled as an expectation. This is the disqualification-risk check.
6. **Frozen-boundary check** — diff Pendahuluan and the core-problem statement against the
   Extended Abstract to prove the admin ruling was respected.
7. **Forbidden-content check** — confirm zero occurrences of glove/IMU, analog physical joystick,
   and "aplikasi web"/"smartphone app" as the described interface.
8. **Prior-art honesty check** — the smoothing-is-a-hypothesis caveat and the 2-second-hold-is-
   project-defined caveat are both present.
9. **Title-readiness check** — the provisional title is isolated in one place so the final title
   can be substituted without a rewrite.

### Modules (artefacts) under check

- The paper draft (primary artefact).
- `claim-ledger-dingleberry.md` (the grounding gate).
- The wayfinder ticket answers + ADRs (the decision record the draft must not contradict).
- The guidebook PDF (external authority; cited by page).

### Prior art for these checks

- The existing rubric extraction in `research/01-guidebook-requirements.md`, which already quotes
  the guidebook verbatim with page numbers — checks 1, 2 and 3 reuse it directly.
- The claim ledger, which already separates pre-registered targets from sourced facts and was
  built as exactly this kind of gate.

### The paper's own promised validation (not a check on the draft, but the plan it commits to)

The locked 2×2 protocol, to be executed after this submission: condition (A: baseline PS2 stick vs
B: stick + fine mode) × distance (1 m, 3 m); **40 trials per operator per condition**; **3 paired
operators, fallback 2**; counterbalanced order; 2-second-hold success criterion **8 of 10 on
target**; placement error measured by phone photo against the marked grid; one-way latency
(t_receive − t_send) as a pre-registered in-team target.

## Out of Scope

- **Hardware modification before submission** — no new sensors, no gripper redesign, no reprints.
  Whatever the design commits to must be buildable in the *next* stage.
- **Running any physical experiment as part of this submission** — locked out by the 18 Oct
  prototype constraint. All results in the paper are expectations.
- **Camera-based autonomy** as a designed path — rejected in ADR 0001; appears only as one
  future-work paragraph.
- **The glove/IMU and analog-physical-joystick paths** — rejected by the user; zero mentions.
- **Real fuel-rod handling claims** — the paper is a tabletop proof of concept and must say so.
- **Anything beyond this competition submission** — publication, other contests, productisation.
- **The final title itself** — deliberately left open (GitHub Issue #1); the paper proceeds with a
  provisional title. This is the one decision the effort is not closing here.

## Further Notes

- **Provisional-title discipline.** The title is the only unsettled paper-level decision. Draft
  freely, but keep the title in exactly one place so it can be replaced in one edit. It must not
  contain "aplikasi web" / "smartphone app".
- **Sender platform resolved (16 Oct):** the one genuine blocker is cleared — the Metodologi
  architecture subsection and the Feasibility cost sentence can now be drafted (sender = commodity
  laptop, UDP transport). The title is now the only open paper-level item.
- **Unverified price.** Rp40k–70k is a team estimate. A real wired-PS2 listing link should be
  captured before the figure enters the paper; otherwise keep the estimate label.
- **Unsettled factual question for the team:** whether the arm physically exists as a *built*
  prototype. There is no digital evidence in this tree (no photos, no firmware, no STL), yet the
  Extended Abstract states build steps in past tense. The wording of Hasil dan Pembahasan depends on
  the answer — treat as a question for the team, not something to assume.
- **Tracker doc drift (not blocking):** `AGENTS.md` declares a root `GLOSSARY.md` and `docs/adr/`,
  but neither exists — the ADRs live in `.scratch/spc-full-paper/adr/` and there is no glossary.
  Worth fixing so the domain-modeling skill has the paths it expects.
- **Mirror:** the GitHub mirror at `AstraxCode/spc-eureka-2026-wayfinder` is a snapshot of the
  tracker; re-sync it after the drafting sessions so teammates never read a superseded decision.
