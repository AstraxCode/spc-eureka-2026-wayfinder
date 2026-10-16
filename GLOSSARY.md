# SPC Eureka 2026 full paper — domain language-archonx

The working vocabulary for the SPC Eureka! ITB 2026 full paper: a teleoperated tabletop 5-DOF arm
that places objects accurately while the operator stands away from the source. Every ticket,
ticket answer, and paper section uses these terms with exactly these meanings; a synonym listed
under _Avoid_ is drift and must not appear in the paper.

Authority for the decisions behind these terms: `map.md`, `issues/`, `spec.md`, and the ADRs in
`.scratch/spc-full-paper/adr/`.

## Control paradigm

**Teleoperation**:
A human operator commands the arm from a distance and stays in the control loop for every movement;
no part of the task is executed autonomously.
_Avoid_: autonomous control, automatic control, "manual mode".

**PS2 controller**:
The committed input device: one hand-held pad carrying an analog stick, ABXY buttons, and a
trigger. The stick is the only continuous input; ABXY and the trigger change what the stick drives.
_Avoid_: gamepad, any screen-based interface wording (superseded by the PS2 decision — the
prohibited strings are listed in `spec.md` → Testing Decisions, check 7), glove, IMU.

**fallback**:
A documented alternative used only if the primary path proves unworkable at build time — never the
interface the paper describes as its design. The fallback chain is the ESP32-hosted web joystick,
then Blynk Cloud behind it; the PS2 controller is the primary path.
_Avoid_: alternative design, option B, plan B.

**Stick**:
The PS2 controller's analog input, used as a **rate** control: stick displacement commands a
velocity, so stick centred commands zero velocity. Pushing the stick forward drives the
end-effector forward, with several joints coordinated by firmware; selecting a joint with ABXY
instead drives only that joint.
_Avoid_: joystick (when the controller as a whole is meant), virtual joystick, position control.

**Coarse mode**:
The baseline control layer, active whenever fine mode is off: the full command-to-joint gain, so a
given stick displacement produces the full-scale joint motion. Used to approach the target.
Indonesian paper term: *mode kasar*.
_Avoid_: normal mode, fast mode, default mode.

**Fine mode**:
The paper's contribution: an operator-triggered control layer, toggled by the controller's trigger,
that lowers the command-to-joint gain so a given stick displacement produces a smaller joint motion
near the target. Paired with release-to-hold. Indonesian paper term: *mode halus*.
_Avoid_: smoothing, filtering, adaptive mode, bubble mode, clutch, position control.

**Gain reduction**:
The mechanism inside fine mode: the command-to-joint scale factor is lowered, so the same stick
displacement maps to a smaller joint motion. Motion scaling is its literature precedent; the
numeric factor is a firmware parameter, not a paper claim.
_Avoid_: scaling, sensitivity, resolution multiplier.

**Release-to-hold**:
Returning the stick to centre commands zero velocity, so the arm stops and holds its last commanded
position with no drift. Under stick rate control this is inherent; the paper presents it as the
software replacement for the hardware clutch used in the literature.
_Avoid_: brake, freeze, lock, hardware clutch, re-centring.

**Open-loop**:
The receiver drives the servos without position feedback: no encoders, no current sensing, no new
sensors. The commanded PWM is assumed to be achieved, so precision comes from the operator-side mode
and the firmware limits, not from measurement.
_Avoid_: closed-loop, feedback control, sensorless.

## Control chain

**receiver ESP32**:
The microcontroller on the arm that turns incoming commands into servo-driver outputs for the
servos. Unchanged by this work: open-loop, no new sensors.
_Avoid_: slave, target board.

**sender-side ESP32**:
The microcontroller on the operator's side: it polls the PS2 controller (four-wire interface, PS2X
library), runs the three control layers, and transmits commands over Wi-Fi to the receiver ESP32.
Retained by the 16 Oct ticket-09 decision; it is a part the team already owns, which is what the
Feasibility argument now rests on instead of the retracted "sender ESP32 removed" saving.
_Avoid_: master, transmitter, gateway.

## Evaluation

**Operator**:
A person who runs the trials and moves the arm. Three paired operators are planned, each running all
four cells, with a documented fallback of two.
_Avoid_: subject, user, tester.

**Condition A**:
Baseline PS2 stick control — coarse mode only, no fine mode.
_Avoid_: control group, coarse condition.

**Condition B**:
PS2 stick control with fine mode available.
_Avoid_: treatment, intervention condition, fine condition.

**Placement error**:
The distance between the object's centre and the target's centre after a placement, read on the
marked grid. One of the three retained metrics.
_Avoid_: accuracy, precision, positional deviation.

**Grid cell**:
One marked cell of the placement grid on the work surface, used to read placement error from a phone
photo against the grid markings. "Within one grid cell" is the pre-registered placement target, and
its numeric value is derived from the measured grid spacing — never invented.
_Avoid_: square, tile, zone.

**2-second hold**:
The project's success criterion for a placement: the object stays on target for two seconds. A run
passes at 8 of 10 trials on target. **Project-defined** — never described as a standard
telemanipulation metric.
_Avoid_: dwell time, settling time, standard hold metric.

**One-way latency**:
The time for one command to travel from the operator's input to the receiver's action, measured as
t_receive − t_send. One of the three retained metrics; reported as a pre-registered in-team target,
never as a literature number.
_Avoid_: round-trip time, ping, end-to-end delay.

**Pre-registered target**:
A numeric value the team commits to before collecting data, stated as a target in advance and never
as a result. Current targets: one-way latency ≤ 200 ms; placement error within one grid cell.
_Avoid_: goal, estimate, expected value.

**Expected result**:
Any result-shaped statement in the paper that is a design-based prediction rather than a
measurement, labelled as an expectation where it appears. Pre-registered targets are its numeric
subset.
_Avoid_: preliminary result, projected result, estimated result.

**team estimate**:
A figure supplied by the team without a captured listing or source behind it. It may enter the
paper only carrying this label. Currently only the PS2 controller price (Rp40k–70k).
_Avoid_: price, cost (unlabelled).

## Working conventions

**`-archonx`**:
The internal watermark suffix this effort appends to the paper's title and every section header, and
to the working documents behind it, to mark them as in-development drafts.
