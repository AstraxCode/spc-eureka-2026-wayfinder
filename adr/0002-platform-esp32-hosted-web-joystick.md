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
