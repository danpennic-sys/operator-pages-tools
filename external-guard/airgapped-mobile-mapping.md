# Mapping: Guard Interface Contract → Air-Gapped Mobile Product

Target product: **QuantumGuard Mobile Verifier**  
(Offline single-verifier evidence gate. PASS / FAIL / INDETERMINATE. Ed25519 frozen.)

We do not promise correctness. We prove it.

---

## 1. Product Context

| Element | Instantiation |
|---------|---------------|
| Protected binary | QuantumGuard Mobile Verifier (unmodified) |
| Guard | Minimal External Guard runtime, provisioned via physical media |
| Environment | Hardened Android / air-gapped mobile device |
| Network after provision | None |

Binary stays untouched. Guard enforces the Contract.

---

## 2. Zone Mapping

### Zone A — Operator → Guard

| Contract Call | Mobile Instantiation |
|---------------|----------------------|
| Load_Invariants | Loaded from physical media (SD / USB-OTG / signed package) |
| Provision_Attestation | Guard verifies its own attestation block |
| Bind_Target | Static preload or external monitor. Binary never modified. |
| Arm | Invariants locked. Post-arm injection forbidden. |
| Execute | Operator launches Verifier. Guard observes. |

### Zone B — Guard → Binary

Allowed: Observe_Memory, Observe_ControlFlow, Observe_EvidenceChannels.  
Forbidden: any patch, rewrite, or injection.

### Zone C — Guard → Operator

| Output | Mobile Behavior |
|--------|-----------------|
| OK | Verifier completed within invariants |
| FAIL(code) | Stable local failure code |
| EVIDENCE(block) | Bounded, deterministic, device-local evidence |
| HALT | Verifier terminated. Device remains in known state. |

No warnings. No soft errors. No off-device telemetry.

---

## 3. Function Instantiation

| Function | Air-Gapped Mobile Behavior |
|----------|----------------------------|
| Load_Invariants(set) | Only from attested physical media. Incomplete → FAIL. |
| Bind_Target(binary) | Reproducible. Failure → FAIL. |
| Arm() | Invariants immutable. Enforcement begins. |
| Execute() | Any violation → immediate trap. |
| Emit_Evidence() | Local, bounded, deterministic block. |

---

## 4. Deterministic FAIL Surface

On violation:

1. FAIL(code)  
2. EVIDENCE(block) written to local storage  
3. HALT  

Operator recovers evidence via physical media or local console only.

---

## 5. Provisioning Path

```
Physical media
    → Guard binary + attestation
    → Invariant set
    → Bind to QuantumGuard Mobile
    → Arm
    → Execute
```

After this sequence the device never needs external connectivity to enforce the Contract.

---

## 6. Operator Summary

- Binary remains the frozen QuantumGuard Mobile Verifier.  
- Guard is the only enforcement surface.  
- All interaction follows the three Zones.  
- FAIL is local, deterministic, and treated as a safety success.  
- Everything after initial provision works offline.
