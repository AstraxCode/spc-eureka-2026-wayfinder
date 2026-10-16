# ADR 0001 — Reject camera-based autonomy for the full-paper design

Status: accepted (2026-10-14)
Context: ticket 06 (control paradigm), SPC Eureka 2026 full paper.

## Decision

The full paper commits to Blynk-app control (custom in-app joystick, self-hosted local Blynk
server for latency-sensitive mode, sender ESP32 removed). Camera-based autonomous grasping
(camera identifies object and target; robot plans and executes grasp/place) is rejected for this
submission and recorded as future work.

## Why it lost

- **Evidence fit (decisive):** no physical trials are possible before submission (hard constraint);
  the prior-art sweep found no support we could cite for vision-based grasping on this class of
  hardware. The paper would have to argue an autonomy claim from design intuition alone.
- **Hardware fit:** requires adding a camera plus sufficient compute for object detection to the
  NEXT stage's build — cost and complexity the Feasibility rubric row (15%) punishes.
- **Time:** vision pipeline development inside the competition timeline is the worst of the three
  paths.

## What would unblock it

A dedicated literature pass on vision-guided manipulation for low-cost arms; a working camera +
detection demo before the Final stage (28–29 Nov 2026); budget approval for camera and compute.

## Consequences

- The map's metrics line ("presumes teleoperation") stays intact: Blynk control remains human
  teleoperation, so placement error, 2-second hold and one-way latency are all retained.
- Future-work paragraph of the paper: camera-based autonomy as the long-term path toward reducing
  operator load, contingent on the unblockers above.
- AMENDED 2026-10-15 (ticket 04 interview): the manual glove/IMU path is rejected outright per
  user decision — the paper's committed interface is digital control on a phone (ESP32-hosted web
  joystick per ADR 0002); glove/IMU appears nowhere as a committed or alternative interface.
- AMENDED 2026-10-16 (recording the 2026-10-15 PS2 pivot): the "digital control on a phone /
  ESP32-hosted web joystick" interface named in the amendment above is itself SUPERSEDED. The
  committed input device is now a PS2 controller (ticket 06 amendment 2; ADR 0002 amendment).
  The glove/IMU rejection stands — zero mentions in the paper. Camera autonomy remains the
  future-work paragraph, and the human-teleoperation premise that keeps all three metrics alive
  is unchanged.
- AMENDED 2026-10-16 (ticket 09): the "sender ESP32 removed" clause in the Decision above is
  RETRACTED — the sender-side ESP32 is retained (ticket 06 amendment 3; ADR 0002 amendment 2).
  The Decision text is left as written because ADRs are append-only; nothing else in it is live.
