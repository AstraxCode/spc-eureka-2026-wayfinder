# ADR 0002 — Control platform: ESP32-hosted web joystick, Blynk as fallback

Status: accepted (2026-10-14)
Context: tickets 06/07; amends the platform decision in ticket 06's answer.

## Decision

The operator interface is a **self-hosted web joystick served directly by the receiver ESP32**
over the local Wi-Fi network: the phone's browser opens the ESP32's page, which presents a canvas
joystick, an explicit fine-mode button, and a gain/scale control. No sender ESP32, no cloud, no
app install. **Blynk Cloud (option a) is retained as the documented fallback** if the web-joystick
path proves unworkable at build time.

## Why Blynk lost the primary slot (after initially winning ticket 06)

- Ticket 07 research: current Blynk IoT has **no public self-hosted server** (Enterprise-only;
  Legacy local server + apps retired Dec 2022), so the "self-hosted local server" latency
  mitigation the user chose in ticket 06 is not available on the current platform.
- The app-to-arm link is therefore always cloud-mediated: Legacy-era community pings of
  85–383 ms and the docs' <200 ms guideline fight the paper's headline one-way-latency metric.
- Third-party rate limits (10 values/s flood, 20 req/s disconnect) and undocumented joystick
  widget send-rate constrain real-time control.
- Infrastructure dependence is itself a design weakness for the radiation-scenario use case.

## What the ESP32-hosted path preserves

App-based control, sender ESP32 removed, in-app fine-mode button, gain reduction + release-to-hold
latch, full link control (local LAN latency only), zero per-operator install. Cost: the UI lives
in firmware (plain look, browser touch latency slightly higher than native).

## Fallback trigger

If the web joystick cannot meet the pre-registered latency target in in-team testing, the paper
falls back to Blynk Cloud with latency reported as a measured, pre-registered target
(claim-ledger convention), not a result.
## Amendment 2026-10-15 (recorded 2026-10-16) — superseded as the primary interface

The PS2-controller decision (tickets 06 and 02, same day) supersedes this ADR's **Decision**: the
operator interface is a **PS2 controller** (analog stick + ABXY + trigger), not the ESP32-hosted
web joystick. Status is now **superseded-as-primary, retained-as-fallback** — the ESP32-hosted web
joystick remains the documented fallback if the PS2 path proves unworkable at build time, exactly
the role Blynk Cloud plays in the Decision above.

Surviving intent: cloud-free, app-free local control; an explicit fine-mode control; gain
reduction + release-to-hold latch; zero per-operator install; the Blynk-Cloud fallback chain.

NOT settled by this amendment: whether a **sender-side ESP32** is retained. The PS2 controller
needs a master MCU to read it (PS2X library), so ticket 06's original "sender ESP32 removed" cost
claim cannot hold as written. That re-decision belongs to ticket 06 and must land before the
Metodologi architecture section is drafted.

## Amendment 2 — 2026-10-16 (ticket 09 resolved): the sender-side ESP32 is RETAINED

The question the amendment above left open is settled: the **sender-side ESP32 is retained**. It is
the master MCU that reads the PS2 controller (four-wire polled interface; PS2X library) and
transmits commands over Wi-Fi to the receiver ESP32. Without it the operator side has no host,
because a PS2 pad has no radio and only answers polls — so "no sender MCU" would require
reverting the interface to a screen, which this ADR already demoted.

The two fallbacks are unchanged: the **ESP32-hosted web joystick** remains the documented fallback
to the PS2 primary, with Blynk Cloud behind it.

Ticket 06's original "sender ESP32 removed" cost saving is retracted (ticket 06 amendment 3). The
Feasibility argument now rests on the sender ESP32 being an already-owned part (2x ESP32 in the
inventory) plus the glove hardware that is no longer needed. Chain: PS2 controller → sender ESP32 (PS2X) → Wi-Fi → receiver ESP32 → PCA9685 → MG996R servos.

