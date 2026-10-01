# Operator Pages Tools

Lightweight, deterministic operator tools. Normal Mode only. No heavy machinery.

## Current Tools

### Send Invoice + Email Template
`send_invoice_email.py`

Creates a Stripe customer (or reuses one), builds and finalizes an invoice, then creates a Gmail draft containing the hosted payment link and PDF.

**How to use**
1. Edit the CONFIG section at the top of the file.
2. Run the script (or execute the steps via connected tools).
3. Review the Gmail draft and send when ready.

**Defaults**
- Test mode Stripe account: Operator pages
- Collection method: send_invoice
- Days until due: 14
- Draft-first (never auto-sends to customer)

## Design Principles
- One invoice at a time
- External anchors only (no mental load)
- Draft before send
- Metadata tagged `source: operator-pages`
