# 09: Sender-side ESP32 — kept or removed (ticket 06 amendment 2)

**What to build:** Settle whether the sender-side ESP32 is retained under the PS2-controller
scheme. A PS2 controller needs a master MCU to read it (PS2X library), so ticket 06's original
"sender ESP32 removed" cost claim cannot stand as written. Resolving this unblocks the Metodologi
architecture subsection and the Feasibility cost sentence.

**Blocked by:** None (can start immediately — needs team/user input).

**Status:** resolved (2026-10-16)

- [ ] Decision recorded as a **dated amendment in the original ticket 06** (never a silent map
      overwrite), and the ADR set updated if the committed platform changes.
- [ ] The "sender ESP32 removed" cost claim is explicitly upheld (with the PS2 master-MCU path
      explained) or retracted.
- [ ] `map.md` "Not yet specified" item on the sender ESP32 is cleared with a context pointer.
- [ ] The control chain in the paper is internally consistent: controller → MCU → Wi-Fi →
      receiver ESP32 → PCA9685 → servos.

## Resolution (2026-10-16)

Committed by the user: the sender is a **commodity operator-side laptop** under the PS2 scheme —
PS2 controller → PS2-to-USB adapter → laptop → Wi-Fi (**UDP**) → receiver ESP32 → PCA9685 → servos.
No sender MCU is added, so the original "sender ESP32 removed" cost claim stands. Recorded as
**ticket 06 amendment 3** and an **ADR 0002 amendment**; the map's "Not yet specified" sender item
is cleared.

Jitter design measures (network: UDP, dedicated link, power-save off, 5 GHz fixed channel; host:
raw HID, high priority, fixed-rate non-blocking loop, no jitter buffer; design: loss is benign
under rate control + release-to-hold, per-packet timestamps logged). One-way latency stays a
pre-registered ≤ 200 ms target with the OS hop disclosed in the paper's honest-limits.
