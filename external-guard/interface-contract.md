# Guard Interface Contract — External Guard Runtime (Operator Grade)
We do not promise correctness. We prove it.

---

## 1. Contract Scope

The Guard Interface Contract defines the only legal interaction surface between:

- The External Guard (enforcement runtime)  
- The unmodified product binary (protected code)  
- The Operator (authority provisioning invariants and invoking execution)  

No other channels, hooks, rewrites, or implicit behaviors are permitted.

---

## 2. Interface Zones

The contract exposes exactly three zones:

### Zone A — Operator → Guard

Operator provides configuration and invariants.

**Allowed calls:**
- Load_Invariants  
- Provision_Attestation  
- Bind_Target  
- Arm  
- Execute  

**Operator cannot:**
- Modify binary  
- Rewrite Guard  
- Inject dynamic policy after arming  

### Zone B — Guard → Binary

Guard observes. Guard never alters.

**Allowed interactions:**
- Observe_Memory  
- Observe_ControlFlow  
- Observe_EvidenceChannels  

**Forbidden interactions:**
- Patching instructions  
- Rewriting memory  
- Altering control flow  
- Injecting instrumentation  

### Zone C — Guard → Operator

Guard reports deterministic outcomes.

**Allowed outputs:**
- OK — binary remains within invariants  
- FAIL(code) — invariant violation  
- EVIDENCE(block) — local, deterministic, bounded evidence  
- HALT — Guard terminates binary execution  

No warnings. No soft errors. No telemetry.

---

## 3. Contract Functions

**Function: Load_Invariants(set)**  
Input: complete invariant set  
Output: ACCEPT or FAIL  
Rules:
- Must be complete  
- Must be deterministic  
- Must fit within Guard’s auditable footprint  

**Function: Bind_Target(binary_path)**  
Input: path or handle to unmodified binary  
Output: BOUND or FAIL  
Rules:
- Binding must not modify binary  
- Binding must be reproducible  

**Function: Arm()**  
Input: none  
Output: ARMED  
Rules:
- After arming, invariants become immutable  
- Guard enters enforcement mode  

**Function: Execute()**  
Input: none  
Output: runtime state transitions  
Rules:
- Guard observes all critical operations  
- Any violation → immediate FAIL  

**Function: Emit_Evidence()**  
Input: violation context  
Output: deterministic evidence block  
Rules:
- Evidence must be local  
- Evidence must be bounded  
- Evidence must be reproducible  

---

## 4. Deterministic FAIL Contract

On violation, Guard must produce:

- FAIL(code)  
- EVIDENCE(block)  
- HALT  

Codes must be stable across runs.  
Evidence must be identical for identical violation contexts.
