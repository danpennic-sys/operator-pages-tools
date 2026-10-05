# Bind to Runtime
External Guard — Air-Gapped Mobile  
Operator-grade. Deterministic. Non-invasive.

We do not promise correctness. We prove it.

---

## 1. Purpose

Define the only legal ways the External Guard attaches to an unmodified binary so that observation and enforcement can begin.

Binding must:

- Leave the binary completely unchanged  
- Be reproducible across identical devices  
- Fit inside the Minimal Guard Footprint  
- Fail closed if attachment cannot be established  

---

## 2. Allowed Binding Methods

| Method | Description | Air-Gapped Fit |
|--------|-------------|----------------|
| **Static Preload** | Guard is loaded into the process address space before the binary starts | High |
| **External Monitor Process** | Guard runs as a separate process and observes via OS-mediated channels | Medium |
| **Hardware-Anchored Interposition** | Guard is anchored by hardware features (TrustZone, hypervisor, or equivalent) | Highest |

No other binding methods are legal under this contract.

---

## 3. Binding Rules

1. **Non-modification** — Target binary remains bit-identical.  
2. **Reproducibility** — Identical inputs produce identical binding result.  
3. **Fail-closed** — Inability to bind cleanly → FAIL.  
4. **Immutable after Arm** — Binding cannot be changed without full HALT + re-provision.  
5. **Minimal surface** — Only channels required for Observe_Memory, Observe_ControlFlow, Observe_EvidenceChannels.

---

## 4. Bind Sequence (Deterministic)

```
1. Operator supplies bind.conf (method + target handle)
2. Guard verifies target binary identity (hash / attestation)
3. Guard attempts attachment via the declared method
4. Guard confirms observation channels are live
5. Guard returns BOUND or FAIL
```

Any step failure → FAIL.

---

## 5. Mobile Instantiation (QuantumGuard Mobile Verifier)

Preferred order:

1. Static Preload (default)  
2. Hardware-Anchored (when available)  
3. External Monitor (last resort, isolation proven)

Binding configuration is supplied on physical media with the Guard and invariants.

---

## 6. Operator Checklist

```
[ ] Target binary hash verified
[ ] Binding method declared in bind.conf
[ ] Binding attempt executed
[ ] Observation channels confirmed live
[ ] Result is BOUND (or FAIL)
[ ] No modification to the binary occurred
```

---

## 7. One-Sentence Summary

**The Guard attaches without touching the binary.  
If it cannot attach cleanly, it fails.**
