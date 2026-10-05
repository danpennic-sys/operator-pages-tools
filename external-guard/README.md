# External Guard Runtime — Operator Pack

We do not promise correctness. We prove it.

Canonical operator-facing surface for the External Guard.

## Core Triad

| File | Purpose |
|------|--------|
| `doctrine.md` | What it is and the non-negotiable rules |
| `invocation-pattern.md` | How the operator runs it |
| `interface-contract.md` | The only legal interaction surfaces |

## Supporting Specifications

| File | Purpose |
|------|--------|
| `minimal-footprint.md` | Smallest viable Guard that still satisfies the triad |
| `bind-to-runtime.md` | Legal binding methods and rules |
| `airgapped-mobile-mapping.md` | Interface Contract mapped onto QuantumGuard Mobile Verifier |

## Usage Rule

Treat these as the stable operator surface.  
Do not expand them while operating.  
Binary stays unmodified. Guard enforces invariants. FAIL is deterministic and local.
