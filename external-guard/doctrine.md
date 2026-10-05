# External Guard Doctrine
Operator-grade. One page. Normal Mode.

---

## Definition

An **External Guard** is a separate runtime component that enforces hard safety invariants on an unmodified binary.

The protected code never changes.  
The Guard watches critical operations and forces a deterministic FAIL when a rule is broken.

---

## Core Rule

**Source stays the same. Safety lives outside.**

If the product binary must be rewritten to gain the guarantee, it is not an External Guard.

---

## What It Enforces

| Invariant              | Behavior on violation      |
|------------------------|----------------------------|
| Array / buffer bounds  | Immediate trap + FAIL      |
| Allowed memory regions | Trap + FAIL                |
| Control-flow integrity | Trap + FAIL                |
| Evidence integrity     | Trap + FAIL                |
| Policy rules           | Trap + FAIL                |

Silent corruption is forbidden.  
Every violation produces a clear, local, deterministic failure.

---

## Required Properties

1. **External** — lives outside the protected binary  
2. **Deterministic** — same input → same FAIL  
3. **Offline-capable** — works after initial provisioning, no network required  
4. **Auditable** — small enough to inspect and attest  
5. **Loud** — failure is never silent or deferred  
6. **Non-invasive** — protected source remains unchanged

---

## What It Is Not

- Not a language rewrite  
- Not a compiler sanitizer that rewrites the binary at build time  
- Not a cloud service or remote monitor  
- Not a best-effort warning system

---

## Operator Use

- Apply to existing C / legacy / constrained binaries that cannot be rewritten  
- Use when clear FAIL states are mandatory  
- Prefer for air-gapped and mobile environments  
- Keep the Guard itself minimal and provisionable via physical media

---

## One-Sentence Summary

**The product binary stays as written.  
The External Guard makes the safety guarantee real.**

---

Keep this sheet short. Refer to it when needed. Do not expand it while operating.
