# Operator Checklist — Send Invoice + Email

Copy for each run. Keep it external. Do not hold in working memory.

```
[ ] Fill CONFIG values in send_invoice_email.py
[ ] Create customer (PostCustomers)
[ ] Create invoice item (PostInvoiceitems)
[ ] Create invoice with pending_invoice_items_behavior="include"
[ ] Finalize invoice (PostInvoicesInvoiceFinalize)
[ ] Confirm hosted_invoice_url + invoice_pdf are present
[ ] Create Gmail draft (or send)
[ ] (Optional) Internal notify to yourself
[ ] Review draft in Gmail → send when ready
```

## Guardrails
- Always draft-first unless explicitly told to send.
- One invoice at a time.
- Tag metadata source=operator-pages.
- Stay in Normal Mode.
