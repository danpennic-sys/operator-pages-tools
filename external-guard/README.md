# External Guard Runtime — Operator Pack

We do not promise correctness. We prove it.

This directory contains the stable operator triad for the External Guard:

1. **Doctrine** — what it is and the non-negotiable rules
2. **Invocation Pattern** — how the operator runs it
3. **Interface Contract** — the only legal interaction surfaces

Binary stays unmodified. Guard enforces invariants. FAIL is deterministic and local.

## Files

| File | Purpose |
|------|--------|
| `doctrine.md` | External Guard Doctrine |
| `invocation-pattern.md` | Operator Invocation Pattern |
| `interface-contract.md` | Guard Interface Contract |

## Usage

Treat these as the canonical operator-facing surface.
Do not expand them while operating.
