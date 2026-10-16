# Prior art: assistive control for precise teleoperation

## Scope and takeaway

The closest defensible precedent for this project is not autonomous manipulation, but **human-led teleoperation augmented by motion scaling / mode switching**. Published work reports improved task accuracy or efficiency from low or adaptive motion scales, and from hybrid position/rate control. Those systems use instrumented master arms, task/scene information, or haptic devices, so they do not establish that an MPU6050-and-flex-sensor interface will get the same gains. They do, however, justify testing smoothing and a fine-control mode as hypotheses against a manual baseline.

## 1. Filtering/smoothing and measured accuracy

A 2024 IEEE conference paper directly compares eight time-series filters for RGB-D-camera motion-capture teleoperation (Savitzky–Golay, hierarchical threshold, median, Whittaker, weighted sliding convolutional averaging, adaptive, Kalman, and locally estimated scatterplot smoothing). It evaluates time complexity, mean absolute error, variance, and RMSE; in 12 circular-motion experiments, Savitzky–Golay reportedly improved smoothing by 26.74%, with weighted sliding averaging at 24.4%. A handwritten teleoperation test showed smoother filtered trajectories. The abstract does not report a placement-error or target-acquisition study, so this supports reduction of input oscillation, **not a demonstrated task-accuracy improvement** for the proposed arm.[1]

A 2025 arXiv preprint on adaptive motion scaling uses a low-pass filter to smooth the selected scale factor, not the operator's raw command stream. In peg-transfer experiments, adaptive coarse/fine scaling reduced clutch count 38.46%, task completion time 11.96%, and NASA-TLX 58.01% versus one fixed scale. These are encouraging results for smoothing scale transitions and switching scale, but should not be represented as evidence that low-pass filtering user commands alone improves placement accuracy.[2]

**Implication:** compare raw input with at least one explicitly defined smoothing method (e.g. moving average or low-pass), retain the same scale and interface otherwise, and measure placement error and task duration. The cited filter study does not determine the right filter or parameters for IMU-derived orientation data.

## 2. Fine positioning, position/rate control, clutching

Lee et al. (2024) proposed a user-controlled variable-scaling framework, with position and impedance scaling selected according to contact/non-contact task phase. Their abstract reports reductions versus fixed scaling in contact force (48.9%), completion time (20.2%), and NASA-TLX (36.6%). Full text was not accessible in the extracted page; these abstract-level figures and the study design details should be checked against the article before quoting them in a formal paper. URL: https://link.springer.com/article/10.1007/s12555-022-1099-z

A 2022 open-access *Applied Sciences* study in a nuclear-fuel-handling teleoperation task explains the key compromise: low position scale enables precise, high-resolution movement but requires more indexing/clutching; high scale enables faster approach but reduces resolution; rate control approaches the target conveniently but has poorer transparency near it. It describes the “bubble” strategy from prior literature: rate control outside the bubble for coarse movement and position control inside it for fine positioning. Its own task-decomposed position–rate hybrid controller reduced completion time 17.23% and NASA-TLX 34.02% compared with conventional position control.[3]

Richter, Orosco, and Yip (2019) tested three motion-scaling solutions with 17 participants on a da Vinci system under delay. The positional strategy lowers scale as the slave approaches an obstacle; the velocity strategy increases scale with operator speed, allowing low scale during small precise motion and higher scale during fast movement. Their study reports lower error rates for proposed solutions, at the cost of task time; 16 of 17 participants had their best error-rate performance using a proposed solution. This provides a direct precedent for a fine-positioning mode near a target, though its obstacle sensing and surgical setup differ from the team's tabletop arm.[4]

The 2025 adaptive-scale paper also explicitly describes clutching as motion indexing: inappropriate fixed scale either forces repeated clutching when too low, or amplifies small motions and hurts precision when too high. The dynamic controller uses coarse/fine intent classification and a clutch in its leader-arm interface; the experiment reports fewer clutch operations.[2]

**Implication:** a practical first intervention for this project is manual teleoperation plus a switchable fine mode (lower command-to-joint gain near the target), with clear mode feedback. If the interface supports a deadman/clutch button, test whether re-centering/rebinding prevents operator-range exhaustion. No source found here tests rebinding on the specific IMU/wireless interface or establishes a universally optimal switching threshold.

## 3. Accuracy versus latency / filtering delay

The literature located here establishes the broader performance tension for **communication delay and motion scaling**, but does not give a direct numerical accuracy-versus-filter-latency curve for a smoothing filter. Richter et al. describe latency as causing slower operations, reduced movement precision, and increased human error; their proposed motion-scaling methods reduce errors under high delay but their study observes an error/time tradeoff. In their positional-scaling method, scale decreases near obstacles, restricting slowing to regions requiring precision.[4]

The 2024 filter comparison reports computational complexity and trajectory error measures but its accessible abstract does not report end-to-end command latency, phase lag, or a user-task accuracy-versus-filter-delay curve.[1] The adaptive-scale preprint applies an LPF to scaling factor with a user-adjustable convergence speed, but does not establish a raw-command filter latency tradeoff.[2]

**Interpretation for the experiment:** distinguish network one-way latency from local filter-induced delay. Report them separately, define the one-way measurement method (clock synchronization or round-trip/2 with assumptions), and measure filter response/settling or command-to-motion lag. Do not claim that filtering increases latency by a particular amount without measuring it. Compare accuracy and completion time across filter settings; a smoother command that arrives or responds too late may impair correction, but direct quantitative evidence for this exact tradeoff was not found.

## 4. Measures and alignment with project metrics

Published measures found in the directly relevant studies include: filter reconstruction error (MAE, variance, RMSE) and computational complexity; completion time; error rate; contact force; number of clutch operations; and NASA-TLX workload.[1][2][3][4] In the high-delay surgical study, performance used task time and an error metric; the filter paper's errors are trajectory-to-reference metrics rather than target placement errors.[1][4]

A two-second stable hold is a reasonable **project-defined success criterion**, but no source found in this retrieval established it as a standard telemanipulation metric. Likewise, no source found here demonstrates that Fitts-law throughput is a standard metric across robot-arm telemanipulation studies; do not label it standard on this evidence. If the team wants a Fitts-style analysis, define target distance and width, trial completion time, and success/error conditions explicitly and present it as an additional human-interface measure, not a substitute for task-specific placement accuracy.

Recommended alignment: (a) final placement error in physical units and success rate within a predeclared tolerance; (b) time to complete placement, plus time within the 2-second hold condition; (c) one-way network latency and local filtering/command response delay reported separately; and optionally (d) clutch count and NASA-TLX to compare with prior work. Report distributions and repeated trials, not only a single best run.

## Evidence gaps

- No direct task-accuracy result for command smoothing alone was found; the closest filter study evaluates signal smoothness/error and demonstrates a handwriting example.
- No numeric filter-induced-latency versus placement-accuracy study was found in this search.
- No verified Fitts-law/throughput standard for the particular telemanipulation task was found.
- No direct published test found for smoothing IMU wrist-orientation commands paired with flex-sensor grip on a low-cost 5-DOF ESP32 arm.
- The variable-scaling Springer paper was accessible at abstract level only in extraction; full-text access is paywalled.

## Sources

[1] Zixiong Wang, Yinlong Zhang, and Xin Zhang, “A comparative study on human motion smoothing filters for RGB-D camera teleoperation,” IEEE, 2024 30th International Conference on Mechatronics and Machine Vision in Practice. Abstract/full metadata page: https://ieeexplore.ieee.org/abstract/document/10746144. (IEEE full paper access restricted in retrieval.)

[2] Jeonghyeon Yoon et al., “A Single Scale Doesn’t Fit All: Adaptive Motion Scaling for Efficient and Precise Teleoperation,” arXiv:2503.01216v1 (2025). https://arxiv.org/abs/2503.01216v1

[3] JiWoong Han and Gi-Hun Yang, “Improving Teleoperator Efficiency Using Position–Rate Hybrid Controllers and Task Decomposition,” *Applied Sciences* 12(19), 9672 (2022). https://www.mdpi.com/2076-3417/12/19/9672

[4] Florian Richter, Ryan K. Orosco, and Michael C. Yip, “Motion Scaling Solutions for Improved Performance in High Delay Surgical Teleoperation,” ICRA (2019), arXiv:1902.03290. https://arxiv.org/abs/1902.03290

[5] Hunjo Lee, Jiwoong Han, and Gi-Hun Yang, “Development of Variable Scaling Teleoperation Framework for Improving Teleoperation Performance,” *International Journal of Control, Automation, and Systems* 22, 936–945 (2024). Abstract accessible; full text subscription content. https://link.springer.com/article/10.1007/s12555-022-1099-z

## Coverage counts

- Q1 (filtering/smoothing and accuracy): 2 sources; direct task-placement accuracy evidence absent.
- Q2 (fine positioning, rate/position, clutch/rebinding): 4 sources; specific IMU rebinding implementation not found.
- Q3 (accuracy–latency tradeoff): 3 sources; filter-specific quantitative latency curve not found.
- Q4 (metrics and standards): 4 sources; Fitts-law use as a standard telemanipulation metric not found.
