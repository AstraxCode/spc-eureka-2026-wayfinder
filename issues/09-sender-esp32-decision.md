# 09: Sender-side ESP32 — kept or removed (ticket 06 amendment 2)

**What to build:** Settle whether the sender-side ESP32 is retained under the PS2-controller
scheme. A PS2 controller needs a master MCU to read it (PS2X library), so ticket 06's original
"sender ESP32 removed" cost claim cannot stand as written. Resolving this unblocks the Metodologi
architecture subsection and the Feasibility cost sentence.

**Blocked by:** None (can start immediately — needs team/user input).

**Status:** resolved

- [x] Decision recorded as a **dated amendment in the original ticket 06** (never a silent map
      overwrite), and the ADR set updated if the committed platform changes.
- [x] The "sender ESP32 removed" cost claim is explicitly upheld (with the PS2 master-MCU path
      explained) or retracted. — **RETRACTED** (ticket 06 amendment 3).
- [x] `map.md` "Not yet specified" item on the sender ESP32 is cleared with a context pointer.
- [x] The control chain in the paper is internally consistent: controller → MCU → Wi-Fi →
      receiver ESP32 → PCA9685 → servos.

## Answer (resolved 2026-10-16 — decision confirmed by the user)

**Decision: KEEP the sender-side ESP32, and RETRACT ticket 06's "sender ESP32 removed" cost claim.
The Feasibility argument is re-based on the fact that the sender ESP32 is a part the team already
owns.**

### Why "removed" cannot stand under the committed input device

Ticket 06's original saving was valid for the *phone* interface: the phone was simultaneously the
operator's input surface and the Wi-Fi transmitter, so nothing was needed on the operator side.
The 15 Oct PS2 pivot deleted the phone. A PS2 pad has no radio of its own and no way to originate
network traffic; it only answers polls from a host MCU over a proprietary SPI-like protocol (the
wireless clones add a 2.4 GHz dongle that presents the same protocol). With no sender MCU there is
nothing on the operator side that can read the stick at all, so "sender ESP32 removed" is reachable
only by changing the input device back to a screen — which the team demoted to documented fallback
on 15 Oct (ticket 06 amendment 2; ADR 0002 amendment).

Tethering the pad to the receiver ESP32 on the arm is not a substitute: teleoperation exists so the
operator stands away from the source, and a wired pad on the arm's board puts the operator at the
arm. That is the opposite of the paper's premise.

### The cost argument that survives — and is stronger

| Item | Status | Where it comes from |
|---|---|---|
| Sender-side ESP32 | **already owned** — the inventory carries 2× ESP32 | ticket 06 criterion 2 ("we own 2x ESP32") |
| Glove input hardware (5× MPU6050 + flex sensor) | **not needed** — this is the real saving | ticket 06 amendment (glove rejected 15 Oct) |
| PS2 controller | Rp40k–70k, **team estimate** — must carry that label | `map.md` price fact; pitch doc |

So the Feasibility sentence changes from *"we removed an MCU to cut cost"* to *"the interface change
adds no MCU purchase — the sender ESP32 is a part the team already owns — and it removes the need
for the glove's five IMU units and flex sensor."* The first is not defensible, because it describes
a configuration the committed input device cannot run in. The second is, and Feasibility is 15% of
the rubric.

### Consequences the decision pushes into other tickets

1. **The three control layers live in the sender ESP32's firmware.** Ticket 06 amendment 2 and
   ticket 02's amendment place coordination kinematics and the trigger-toggled gain reduction on
   the "sender side"; with the phone gone, that side *is* the sender ESP32. Ticket 13's architecture
   subsection must say so, and any "implemented in the app" wording is dead.
2. **One-way latency needs an explicit stamping point.** The metric is `t_receive − t_send`
   (GLOSSARY). With a sender MCU in the path, `t_send` must be stamped at the sender's stick-read,
   so the PS2X polling interval sits *inside* the measured path. It is identical in conditions A and
   B, so it does not bias the comparison. Ticket 13 must state the stamping point, and ≤ 200 ms stays
   a pre-registered in-team target, never a result.
3. **One new sourced claim enters the ledger.** "A PS2 controller needs a host MCU, and a public
   PS2X library exists for ESP32" is **not** in `claim-ledger-archonx.md` — that ledger predates the
   PS2 pivot. The pitch doc sources it to `github.com/MyArduinoLib/Arduino-PS2X-ESP32` and an
   electropeak wiring tutorial: tertiary sources, to be graded and added before the claim is written
   into Metodologi. **No polling-rate figure may be stated** — none has been measured.
4. **"<Rp50.000" is a target, not a price.** Ticket 06 amendment 2 and the pitch both carry it as a
   target; the only live-verified figure is the wireless class at Rp85k+ (15 Oct Tokopedia sweep).
   The paper states the wired-clone Rp40k–70k **team estimate** or nothing.

### Records written (all landed 2026-10-16)

- **Ticket 06, amendment 3 (dated)** — records the decision, retracts the "sender ESP32 removed"
  cost claim and states what replaces it, keeps the human-teleoperation premise and all three
  metrics.
- **ADR 0002, amendment 2** — the platform line: the sender-side ESP32 is **retained** as the master
  MCU that reads the PS2 controller; the ESP32-hosted web joystick stays the documented fallback.
  ADR 0002's existing amendment names this exact question as the one it does not settle.
- **ADR 0001** — no change; its human-teleoperation premise still holds.
- **`map.md`** — the "Not yet specified" sender item cleared, with the decision appended to
  "Decisions so far" and a pointer to this ticket.
- **`spec.md`** — the **OPEN** item under "Control interface and architecture" and the "one genuine
  blocker" note in Further Notes resolved; the Feasibility cost sentence rewritten per above.
- **`GLOSSARY.md`** — `sender-side ESP32` redefined as settled (the master MCU that reads the PS2
  controller and transmits over Wi-Fi), dropping the "not yet decided" clause.

### Acceptance checks for the resolution

- Control chain stated once and consistently: **PS2 controller → sender ESP32 (PS2X) → Wi-Fi →
  receiver ESP32 → PCA9685 → MG996R servos** (verified by grep after the records land).
- The string "sender ESP32 removed" is **retracted**, not merely contradicted elsewhere.
- No unverified price and no unmeasured polling figure appears as fact.

### The alternative, for the record

Removing the sender MCU is still possible, but only by changing the operator-side host: a PS2→USB
adapter plus a laptop/phone running the mapping software. That was drafted and reverted on
2026-10-16 (PR #3 closed, branch deleted). It costs an adapter, a host program, an OS hop in the
latency path, and it breaks ADR 0002's "zero per-operator install" intent — so it needs its own ADR
amendment and a Feasibility rewrite if the team prefers it.

## Verification (run 2026-10-16, after the records landed)

- `grep -rn "sender ESP32 removed"` across the effort returns only **retractions or historical
  records**, never a live claim: ticket 06 amendment 3 (retraction), ticket 04 (struck-through
  pointer), ADR 0001 (retraction note), ADR 0002 (its historical text, closed by amendment 2),
  `map.md` (historical + retraction), `spec.md` (retraction), `GLOSSARY.md` (the phrase inside the
  new definition), `WORKFLOW-paper-development.md` (struck through).
- The chain string is present and identical in `map.md`, `spec.md`, ticket 06 amendment 3, ADR 0002
  amendment 2: PS2 controller → sender ESP32 (PS2X) → Wi-Fi → receiver ESP32 → PCA9685 → MG996R servos. (`GLOSSARY.md` defines the chain's nodes individually and does not repeat the full string.)
- `map.md` "Not yet specified" no longer lists the sender-side ESP32; the decision is in
  "Decisions so far" with a link to this ticket.
- `spec.md` carries no OPEN item for the sender; its Further Notes blocker line is closed.
- Ledger: source **S8** plus claims **C11** (a host MCU is required), **C12** (price = team estimate)
  and **C13** (the sender ESP32 is already-owned inventory) added. The pitch doc's electropeak link
  was fetched and is a **404** — recorded as dead, must not enter Daftar Pustaka.
- Pre-edit backups: `.scratch/_backups/spc-full-paper-20261016-2044/`.

**Not verified — do not read as done:** the PS2X polling rate has never been measured, so no
latency figure may be written; the wired-PS2 price still has no live listing; whether the arm exists
as a built prototype is still an open team question.
