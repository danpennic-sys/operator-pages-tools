# Operator Invocation Pattern — External Guard Runtime
We do not promise correctness. We prove it.

---

## 1. Invocation Context

Operator invokes the Guard only at the boundary where an unmodified binary enters execution.  
No rewriting. No patching. No compiler hooks.  
The Guard attaches, observes, and enforces.

---

## 2. Invocation Sequence (Deterministic Path)

**Step 1 — Provision**  
Load Guard from trusted physical media.  
Verify its attestation block.  
If attestation fails → Deterministic FAIL.

**Step 2 — Bind**  
Bind Guard to the target binary using a stable, reproducible attachment method:

- Static preload  
- External monitor process  
- Hardware-anchored interposition  

Binding must not alter the binary.  
If binding cannot be established → FAIL.

**Step 3 — Declare Invariants**  
Operator supplies the invariant set:

- Bounds rules  
- Memory region map  
- Control-flow graph  
- Evidence channels  
- Policy constraints  

Guard loads invariants into its local enforcement table.  
If invariant load is incomplete → FAIL.

**Step 4 — Arm**  
Guard transitions to armed state.  
From this point forward:

- Every violation → immediate trap  
- Every trap → deterministic FAIL  
- No silent corruption allowed  

**Step 5 — Execute**  
Operator launches the unmodified binary.  
Guard observes all critical operations.  
Binary runs normally unless it violates an invariant.

**Step 6 — Respond**  
On violation:

- Guard traps  
- Guard emits local evidence  
- Guard terminates binary  
- Guard returns deterministic FAIL code  

Operator collects evidence and proceeds with post-FAIL workflow.

---

## 3. Operator Responsibilities

- Maintain invariant definitions  
- Keep Guard minimal and auditable  
- Provision via physical media  
- Treat FAIL as a safety success, not a crash  
- Never modify the protected binary  

---

## 4. Invocation Pattern Summary

**Provision → Bind → Declare → Arm → Execute → Respond.**  
Binary stays untouched. Guard enforces reality.
