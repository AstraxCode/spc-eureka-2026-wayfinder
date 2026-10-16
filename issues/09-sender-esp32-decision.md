# 09: Sender-side ESP32 — kept or removed (ticket 06 amendment 2)

**What to build:** Settle whether the sender-side ESP32 is retained under the PS2-controller
scheme. A PS2 controller needs a master MCU to read it (PS2X library), so ticket 06's original
"sender ESP32 removed" cost claim cannot stand as written. Resolving this unblocks the Metodologi
architecture subsection and the Feasibility cost sentence.

**Blocked by:** None (can start immediately — needs team/user input).

**Status:** ready-for-agent

- [ ] Decision recorded as a **dated amendment in the original ticket 06** (never a silent map
      overwrite), and the ADR set updated if the committed platform changes.
- [ ] The "sender ESP32 removed" cost claim is explicitly upheld (with the PS2 master-MCU path
      explained) or retracted.
- [ ] `map.md` "Not yet specified" item on the sender ESP32 is cleared with a context pointer.
- [ ] The control chain in the paper is internally consistent: controller → MCU → Wi-Fi →
      receiver ESP32 → PCA9685 → servos.
