# Sender-side jitter: design measures (PS2 → laptop → Wi-Fi)

Context: ticket 06 **amendment 3** and the resolution of to-tickets ticket **09**. The operator-side
sender under the PS2 scheme is a **commodity laptop** (PS2 controller → PS2-to-USB adapter →
laptop → Wi-Fi → receiver ESP32 → PCA9685 → servos). This note records the jitter-minimisation
**design** that Metodologi (ticket 13) and the honest-limits subsection reuse.

Status: **design only — no measurements.** No physical trials are possible before 18 Oct 2026 (hard
constraint), so this describes intended measures; one-way latency stays a **pre-registered in-team
target (≤ 200 ms)**, never a measured result.

## Layers and measures

**Network (the biggest avoidable source)**
- **UDP, not TCP** — TCP retransmit stalls and head-of-line blocking are the main OS-link jitter
  source; UDP drops a late datagram instead of stalling.
- **Dedicated Wi-Fi** (own AP/router), nothing else on the network.
- **Disable Wi-Fi power-save** on the laptop (and the ESP32 if configurable) — sleep cycles add tens
  of ms.
- **5 GHz, fixed channel**, background scanning/roaming off; AP close to keep retries rare.

**Host (the laptop)**
- Read the controller via **raw HID**, not the high-level gamepad API.
- **Fixed-rate, non-blocking send loop** (~100–250 Hz) on a monotonic clock; send the **latest**
  state only (drop stale samples); no per-iteration allocations.
- **High thread priority**; high-performance power plan; **USB selective suspend and core parking
  off**; game overlays (Game Bar) off.
- **No jitter buffer** — it smooths jitter by adding latency, the wrong trade for control.

**Design (tolerance, not perfection)**
- Under stick **rate control + release-to-hold**, a late or dropped packet just means the arm holds
  its last command — loss is benign by construction.
- **Timestamp every packet** (`t_send`) and log `t_receive − t_send` so the paper can report the
  **mean latency and its jitter distribution**, not a single figure.

## Honest limitation

A general-purpose OS is not a real-time system, so this link cannot be as deterministic as a
dedicated MCU sender. The OS/host hop is disclosed as a limitation in the paper's honest-limits
subsection. Residual jitter cannot be driven to zero; the goal is a small, characterised, disclosed
distribution.
