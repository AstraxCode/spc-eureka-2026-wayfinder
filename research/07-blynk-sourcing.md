# Blynk sourcing: cloud vs local server, offline behaviour, update-rate limits, prior art

## Scope and takeaway

This file covers four questions about using the Blynk smartphone app (custom joystick UI) to command a tabletop 5-DOF ESP32 arm: (1) command/control latency on Blynk Cloud vs a self-hosted local server, (2) whether the app-to-server link works without internet, (3) virtual-pin/joystick update-rate limits relevant to real-time control, and (4) published Blynk-driven robot-arm precedents for the Dasar Teori section.

**Critical platform caveat first:** the team's plan assumes a "self-hosted local Blynk server" is freely available. Under the *current* Blynk platform (Blynk IoT / "Blynk 2.0", launched May 2021), **there is no public self-hosted server**. The freely self-hostable server belongs to the retired **Blynk Legacy (0.x / blynk-server-java)** platform, whose cloud servers were switched off on 31 December 2022, whose mobile apps were removed from the App/Play stores, and whose server code is no longer maintained.[1] Per the Blynk IoT FAQ (Dec 2022): "Is there a Blynk IoT version of Local Server available? — No. Business subscribers may be able to have an 'on premise' server installed, but there is no IoT equivalent of the current Legacy local server."[1] Blynk's current pricing page offers self-hosted/on-premise only in the Enterprise tier; third-party 2026 reviews agree it "targets enterprise customers and is not realistically accessible to individual makers or students."[2][3] **Implication (recommendation):** a genuinely offline local deployment with the *current* Blynk app is not achievable at student cost; the realistic options are (a) Blynk Cloud deployment (internet always required), or (b) a Legacy local server + sideloaded Legacy APK, which is unsupported, unpatched, and may not run on current phone OSes — the FAQ explicitly advises against it.[1] This trade-off must be stated honestly in the paper.

## 1. Blynk Cloud vs self-hosted local server latency

**No peer-reviewed or official benchmark with numbers for local-server Blynk command latency was found.** The sourced quantitative evidence is community-level and indirect:

- Blynk's own troubleshooting docs state that for cloud connections, `ping blynk.cloud` should show **less than 200 ms**; higher ping "could be a reason for disconnections."[4] This is a health guideline, not a command-latency figure.
- A July 2020 Blynk Community thread (robot-over-internet use case, ESP8266 + Blynk Legacy cloud) measured hardware→cloud ping values of ~85 ms (Frankfurt), ~150 ms (New York), ~275 ms (third region) from the user's location, with serial-monitor ping readings varying **135–383 ms** across heartbeats; the user reported "very good responsive maneuvering" via 4G once pinned to the ~100 ms Frankfurt server.[5] Dates and platform (Legacy) must be noted.
- The same thread's key architectural point (community moderator PeteKnight, 24 Jul 2020): a widget change traverses app→server→(hardware polls)→server→hardware, and "a local server, and your phone connected directly to the same network, is the only way to cut-out the variables introduced by the internet."[5] This is qualitative reasoning, **not a measured local-server number**.
- An older community thread (Local Server response time, robot via ESP8266) reports occasional multi-second command delays on a local server and asks for tuning help — evidence that local hosting alone does not guarantee low latency (thread dates to the Legacy era; full content not re-verified in this search pass).[6]
- Blynk markets its cloud as "low-latency access in multiple regions," but publishes no numeric latency SLA on that page.[7]

**Inference (labelled as such):** on one LAN, a local server removes internet round-trips, so app→device latency should be dominated by Wi-Fi and the Blynk protocol heartbeat/poll cycle — plausibly tens of milliseconds rather than the ~100–400 ms cloud figures above — **but no sourced measurement supports a specific local-server number, and the paper must not quote one without running its own experiment.** Recommended: the team measures its own end-to-end command-to-motion latency for both deployment modes and reports the method.

## 2. Offline behaviour of the app-to-local-server link

- For **Blynk IoT (current, 1.x / blynk.cloud)**: the app and hardware both talk to Blynk Cloud. Docs' troubleshooting pages describe failure modes in terms of "no internet connection" and connectivity between device and Blynk.Cloud[4][8]; the current Blynk apps do **not** support pointing at a self-hosted server (see platform caveat above; on-premise is an Enterprise offering[2]). Therefore the current Blynk app **requires internet**; there is no current official offline/local mode for individual users.
- For **Blynk Legacy (0.x)** with the open-source local server (Java/Netty, forwards messages between the app and microcontrollers[9]): community tutorials and threads document running it on a Wi-Fi hotspot / LAN **with no internet access** at all — e.g. "[Tutorial] Blynking offline using esp8266 and WI-FI hotspot," "Using Blynk offline," and "Blynk over local network with no internet access" — confirming the Legacy app + local server path works fully offline once accounts/auth tokens exist (token generation initially needed email access in some setups, a known friction point).[10][11][12] Caveat: these threads date from the Legacy era (pre-2023) and the Legacy apps are no longer downloadable from stores[1]; deployment would rely on previously installed or sideloaded APKs.
- **Version distinction the paper must make:** Legacy Blynk 0.x (blynk-cloud.com, local server possible, offline OK) vs Blynk IoT 1.x (blynk.cloud only for individuals, internet required). Community FAQ confirms Legacy cloud retirement 31 Dec 2022 and no IoT local-server equivalent.[1]

## 3. Virtual-pin / joystick update-rate limits

- Current official docs (Limitations and Recommendations): "If you send more than 10 values per second you may cause Flood Error and your hardware will be automatically disconnected from the server"; don't put `Blynk.virtualWrite` inside `loop()`; use BlynkTimer intervals; avoid `delay()`.[13] (Page last updated ~1 year before retrieval, Oct 2026.)
- Current docs (General Issues): "Blynk Cloud doesn't allow to send more than **20 requests per seconds**. Connections that exceeds the limit are closed."[4]
- Community clarification of the per-pin vs total limits: "**You have 10 req/sec per virtual pin and 100 req/sec total per device**"; widget commands like `LED.on()` count the same as virtualWrite because they are virtualWrite wrappers. (Community answer, Legacy era — figure may differ on current cloud; the current docs give the 20 req/s disconnect threshold above.)[14]
- Joystick widget (current docs): Simple mode sends one datastream per axis (int/double, range = datastream min/max); **Advanced mode sends a single string datastream with X and Y values 0–255**; `BLYNK_WRITE(vPIN)` fires on every update, with `param[0]`/`param[1]` giving X/Y; values are first stored in Blynk.Cloud, *then* forwarded to hardware — i.e. the cloud is always in the data path in Simple/standard use.[15]
- **Implication for control design (recommendation):** the per-pin flood limit means high-rate streaming (e.g. 50 Hz telemetry of five joints) is not feasible per-pin on Blynk Cloud; command direction (app→device, event-driven on joystick move) is the viable path, with joint-state feedback throttled to ≤10 Hz/pin or omitted. No official doc specifies the joystick widget's own send rate on finger movement; that is an **evidence gap** and should be measured empirically.

## 4. Published precedents: Blynk-driven robot arms

Found precedents usable as prior art (verify accessibility/venue quality before citing in the paper; several are lower-tier venues):

- **STM Journals, *Journal of Advances in Embedded Systems Research* (2025):** "IoT-Enabled and Hand Gesture Controlled Robotic Arm Using Blynk IoT and OpenCV" — low-cost multifunction robotic arm with four modes: OpenCV gesture control, Blynk IoT control via ESP32, joystick manual control, and SD-card coordinate playback. Open PDF: https://journals.stmjournals.com/wp-content/uploads/formidable/26/0ab9b35b-36-46-iot-enabled-and-hand-gesture-controlled.pdf (article page: https://journals.stmjournals.com/joaet/article=2025/view=213673/). Closest match to this project's Blynk-joystick mode; read the full text before citing its claims.
- **IJISEM (2025):** "Design and Implementation of an IoT-Based 4-DOF Wi-Fi Controlled Robotic Arm using ESP32 and Blynk Cloud" — 4-DOF arm, ESP32 + Blynk Cloud, design + mathematical modeling. https://www.researchgate.net/publication/405881611_Design_and_Implementation_of_an_IoT-Based_4-DOF_Wi-Fi_Controlled_Robotic_Arm_using_ESP32_and_Blynk_Cloud (PDF also on ijisem.com). Open-access, but venue quality is modest — use as existence-of-precedent, not as a performance benchmark.
- **Semantic Scholar indexed:** Kuppuswamy, Hariharan et al., "Wireless Joystick Control Robotic Arm Using ESP32 Microcontroller" — Wi-Fi robot + arm controlled through the Blynk IoT mobile app. https://www.semanticscholar.org/paper/cef7f74abb6ad812f6ca827a9e48fd3468ff24c6. Direct precedent for Blynk-joystick arm control; details not yet verified from the full text.
- Non-journal but citable as implementation references (grey literature): ESP32 + Blynk joystick robot car repos/examples[16][17] — usable only as informal references, not Dasar Teori citations.

**Note:** no IEEE/MDPI flagship paper combining Blynk joystick control with IMU/flex-sensor glove teleoperation of a 5-DOF arm was found in this pass — which supports the project's novelty framing — but the search was not exhaustive.

## Evidence gaps

- **No sourced numeric latency for a self-hosted local Blynk server** (community or official). The 85–275 ms figures are cloud pings from one user's 2020 Legacy-era test; the <200 ms figure is a cloud health guideline. If the paper discusses local-server latency, it must measure it experimentally or cite nothing.
- No official spec for the **joystick widget's own update/send rate** during finger movement, nor for how Blynk IoT batches/coalesces datastream updates.
- Whether the **10 req/s per pin / 100 req/s per device** figures (community, Legacy era) still hold exactly on Blynk IoT is unconfirmed; the current docs only give the 20 req/s disconnect threshold.
- No current official documentation page confirming offline behaviour of the *current* Blynk IoT app against any self-hosted endpoint — because no such product exists for individuals; the offline claims above rest on Legacy-era community threads.
- Legacy local server "works offline" claims come from community tutorials (2017–2021 era); no current verification on modern Android/iOS versions, and Legacy apps are no longer in stores.
- The three journal precedents were located via search snippets; full texts (especially the STM and IJISEM PDFs) have not been read in this pass — accessibility, dates, and exact claims must be confirmed before citing.

## Sources

[1] PeteKnight, "HELP! Blynk Has Stopped Working! (No Server Connection message)," Blynk Community FAQ, 29 Dec 2022. Legacy retirement 31 Dec 2022; no IoT local-server equivalent; Legacy local server unsupported. https://community.blynk.cc/t/help-blynk-has-stopped-working-no-server-connection-message/64386

[2] Blynk pricing page (self-hosted/on-premise in Enterprise tier). https://www.blynk.io/pricing

[3] "Is Blynk Still Worth It in 2026?" SuperApps (third-party review; self-hosted option targets enterprise). https://superappsdomain.com/is-blynk-still-worth-it/

[4] "General Issues," Blynk Documentation (retrieved Oct 2026; page notes "Last updated 3 years ago"). `ping blynk.cloud` <200 ms guideline; 20 req/s disconnect limit. https://docs.blynk.io/en/troubleshooting/general-issues

[5] "Communication latency" (Solved), Blynk Community, 23–30 Jul 2020. Cloud ping measurements 85–383 ms (Legacy era); local-server/LAN reasoning by moderator. https://community.blynk.cc/t/communication-latency/47446

[6] "Blynk Local Server response time," Blynk Community (Legacy era; occasional multi-second delays reported; not re-verified in full this pass). https://community.blynk.cc/t/blynk-local-server-response-time/11064

[7] "IoT Cloud Platform," Blynk marketing page ("low-latency access in multiple regions"; no numeric SLA). https://www.blynk.io/platform/cloud

[8] "Virtual Pins," Blynk Documentation. https://docs.blynk.io/en/blynk-library-firmware-api/virtual-pins

[9] blynk-server README (open-source Java/Netty Legacy local server, forwards messages between app and microcontrollers). https://github.com/BlynkMobile/blynk-server/blob/master/README.md

[10] "[Tutorial] Blynking offline using esp8266 and WI-FI hotspot," Blynk Community. https://community.blynk.cc/t/tutorial-blynking-offline-using-esp8266-and-wi-fi-hotspot/46959

[11] "Using Blynk offline" (Solved), Blynk Community. https://community.blynk.cc/t/using-blynk-offline/46931

[12] "Blynk over local network with no internet access," Blynk Community. https://community.blynk.cc/t/blynk-over-local-network-with-no-internet-access/10772

[13] "Limitations and Recommendations," Blynk Documentation. 10 values/sec flood limit; BlynkTimer guidance. https://docs.blynk.io/en/blynk-library-firmware-api/limitations-and-recommendations

[14] "Blynk Data Transmission Limits" (Solved), Blynk Community. 10 req/sec per virtual pin, 100 req/sec total per device (Legacy-era community answer). https://community.blynk.cc/t/blynk-data-transmission-limits/44015

[15] "Joystick," Blynk Documentation (app widget; Simple vs Advanced mode, X/Y 0–255 in Advanced). https://docs.blynk.io/en/blynk.apps/widgets-controllers/joystick

[16] ESP32-Blynk-WiFi-Joystick-Controlled-Car (GitHub implementation reference). https://github.com/Saiprasad2004/ESP32-Blynk-WiFi-Joystick-Controlled-Car

[17] "Wireless Joystick Control Robotic Arm Using ESP32 Microcontroller," Semantic Scholar record. https://www.semanticscholar.org/paper/cef7f74abb6ad812f6ca827a9e48fd3468ff24c6

## Coverage counts

- Q1 (cloud vs local latency): 4 sources with quantitative or architectural content; **no local-server latency number exists in any sourced material**.
- Q2 (offline behaviour): 5 sources; offline capability confirmed only for Legacy local server; current Blynk IoT is cloud-only for individuals.
- Q3 (rate limits): 3 sources (2 official docs, 1 community); joystick-widget send-rate spec missing.
- Q4 (prior art): 3 journal/conference candidates + 2 grey-literature refs; full texts unverified.
