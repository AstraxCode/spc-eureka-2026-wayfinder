---
Type: research
Status: resolved
Blocked by:
---

## Question

Source the Blynk-specific claims the paper will need, before any of them is written:

1. Blynk Cloud vs self-hosted local server: typical command round-trip / control latency
   (official docs, community benchmarks, or published papers) — with URLs and dates.
2. Offline behaviour: does the app-to-local-server link work without internet? (Depends on the
   Blynk library/server version — verify against current documentation.)
3. Virtual-pin / joystick widget update-rate limits relevant to real-time control.
4. Any published precedent for Blynk-driven robot-arm control (IEEE/MDPI/arXiv/journals) usable
   as prior art for the paper's Dasar Teori.

Findings to `research/07-blynk-sourcing.md`, every claim with its source URL, gaps flagged
honestly. No latency number enters the paper without a source.

## Answer

Full findings: `../research/07-blynk-sourcing.md` (17 cited sources). Key results:

1. **No sourced numeric latency exists for a self-hosted local Blynk server.** Cloud-side only:
   official docs' <200 ms ping guideline; 2020 community cloud pings 85–383 ms (Legacy era).
   Any local-server latency number must come from an in-team experiment or not appear.
2. **CRITICAL: under current Blynk IoT there is NO public self-hosted server** — on-premise is
   Enterprise-only; the Legacy local server + Legacy apps were retired Dec 2022. The planned
   "self-hosted local server as latency-sensitive mode" is only possible via unsupported Legacy
   0.x with sideloaded APKs; the current Blynk app requires internet. Ticket 06's deployment
   assumption is invalidated and must be re-decided by the user.
3. **Rate limits:** official 10 values/s flood limit, 20 req/s disconnect threshold; Legacy-era
   community adds 10 req/s per pin / 100 req/s per device. Per-pin high-rate streaming is
   infeasible; joystick widget (Simple per-axis int / Advanced X,Y 0–255 string) send rate
   unspecified in docs.
4. **Prior art:** three Blynk+ESP32 robot-arm papers (STM Journals 2025, IJISEM 2025, Semantic
   Scholar-indexed) — all lower-tier venues, full texts unverified; no IEEE/MDPI-level IMU+Blynk
   5-DOF precedent found → supports the paper's novelty claim.

Gaps: all latency figures Legacy-era community measurements; offline behaviour claims rest on
2017–2021 threads untested on current phone OSes; journal precedents located via snippets only.
