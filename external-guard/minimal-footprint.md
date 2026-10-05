# Minimal Guard Footprint Specification
External Guard Runtime — Air-Gapped Mobile  
Operator-grade. Minimal. Deterministic.

We do not promise correctness. We prove it.

---

## 1. Purpose

Define the smallest viable External Guard that still satisfies:

- External Guard Doctrine  
- Operator Invocation Pattern  
- Guard Interface Contract  

Target environment: hardened mobile (Android or equivalent), fully air-gapped after provisioning.

---

## 2. Size & Complexity Constraints

| Constraint | Limit |
|------------|-------|
| Source lines of critical path | ≤ 2 000 SLOC |
| Runtime memory (armed) | ≤ 512 KB |
| Persistent storage (Guard + invariants) | ≤ 1 MB |
| External dependencies | Zero after provisioning |
| Network calls after provision | Zero |
| Dynamic code loading | Forbidden |
| Self-modification | Forbidden |

The Guard must remain small enough to be fully audited by a single operator.

---

## 3. Required Components (No More)

1. **Attestation Block** — Fixed, offline-verifiable identity of the Guard itself.  
2. **Invariant Table** — Loaded once at provision. Immutable after Arm.  
3. **Observer** — Watches only Memory, Control-Flow, and Evidence channels.  
4. **Trap Handler** — On violation: FAIL(code) + EVIDENCE(block) + HALT.  
5. **Evidence Emitter** — Bounded, deterministic, local evidence block.  
6. **Binding Mechanism** — Static preload, external monitor, or hardware-anchored interposition.

No other subsystems are permitted in the minimal footprint.

---

## 4. Forbidden in Minimal Footprint

- Logging beyond the evidence block  
- Telemetry or off-device reporting  
- Soft warnings or degraded modes  
- Policy changes after Arm  
- Just-in-time compilation or rewriting  
- Any network stack  
- General-purpose scripting engine  

---

## 5. Provisioning Footprint

```
/guard/
  guard.bin          # Guard binary
  attestation.blk    # Attestation block
  invariants.tbl     # Complete invariant set
  bind.conf          # Binding method + target handle
```

Total size target: ≤ 1 MB.

---

## 6. Runtime States (Only These)

```
UNPROVISIONED
PROVISIONED
BOUND
ARMED
EXECUTING
FAILED
HALTED
```

No intermediate or soft states.

---

## 7. FAIL Contract (Footprint Level)

On any invariant violation the Guard must, in this order:

1. Record FAIL(code)  
2. Emit EVIDENCE(block) to local storage  
3. HALT the protected binary  
4. Transition to FAILED / HALTED  

Codes and evidence blocks must be stable and reproducible.

---

## 8. Auditability Rule

The entire critical path of the Guard must be readable and understandable by a single trained operator in one sitting.  
If it cannot be audited that way, it is no longer minimal.

---

## 9. One-Sentence Summary

**Small enough to audit, strict enough to enforce, silent about everything except FAIL.**
