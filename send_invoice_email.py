#!/usr/bin/env python3
"""
Operator Pages — Reusable Send Invoice + Email Template
Normal Mode only. One invoice at a time.

Fill the CONFIG section, then execute the flow
(via connected Stripe + Gmail tools or local runner).
"""

from __future__ import annotations
from typing import Any, Dict, Optional

# ---------------------------------------------------------------------------
# CONFIG — change these values for each invoice
# ---------------------------------------------------------------------------
CUSTOMER_NAME   = "Test Design Partner"
CUSTOMER_EMAIL  = "partner@example.com"
ITEM_DESC       = "Operator Pages Design Partner Packet — Setup + first 30 days"
AMOUNT_CENTS    = 150000          # $1,500.00
CURRENCY        = "usd"
DAYS_UNTIL_DUE  = 14
PERSONAL_NOTE   = "Thanks for joining the design partner program."
SEND_AS_DRAFT   = True            # True = Gmail draft, False = send immediately
INTERNAL_NOTIFY = True            # also email yourself a confirmation

# Stripe context (Operator Pages test mode)
STRIPE_CONTEXT  = "acct_1Toz3dKCM4PgZoVF"
LIVEMODE        = False

# ---------------------------------------------------------------------------
# Core flow (map 1:1 to connected tools)
# ---------------------------------------------------------------------------

def create_customer(name: str, email: str) -> str:
    """
    stripe___stripe_api_write
    operation: PostCustomers
    params: name, email, description="Operator Pages", metadata={"source": "operator-pages"}
    Returns: customer_id
    """
    raise NotImplementedError("Call PostCustomers via connected Stripe tool")


def create_invoice_item(customer_id: str, amount: int, description: str) -> str:
    """
    stripe___stripe_api_write
    operation: PostInvoiceitems
    params: customer, amount, currency, description
    Returns: invoiceitem_id
    """
    raise NotImplementedError("Call PostInvoiceitems via connected Stripe tool")


def create_and_finalize_invoice(customer_id: str, days_until_due: int = 14) -> Dict[str, Any]:
    """
    1. stripe___stripe_api_write  PostInvoices
       params: customer, collection_method="send_invoice",
               days_until_due, pending_invoice_items_behavior="include",
               auto_advance=False, description=...
    2. stripe___stripe_api_write  PostInvoicesInvoiceFinalize
       params: id=<invoice_id>
    Returns full invoice object (must contain: id, number, hosted_invoice_url, invoice_pdf, amount_due, status)
    """
    raise NotImplementedError("Call PostInvoices + Finalize via connected Stripe tools")


def draft_customer_email(
    to: str,
    invoice_number: str,
    amount_display: str,
    hosted_url: str,
    pdf_url: str,
    personal_note: str = "",
) -> str:
    """
    gmail_create_draft
    Returns: draft_id
    """
    subject = f"Your Operator Pages Invoice — {invoice_number}"
    body = f"""Hi,

{personal_note}

Your invoice is ready:

Invoice #: {invoice_number}
Amount: {amount_display}
Due: {DAYS_UNTIL_DUE} days from issue

Pay securely here:
{hosted_url}

PDF version:
{pdf_url}

Questions? Just reply to this email.

— Daniel
Operator Pages
"""
    # Call gmail_create_draft(to=[to], subject=subject, body=body)
    raise NotImplementedError("Call gmail_create_draft via connected Gmail tool")


def internal_notify(invoice: Dict[str, Any]) -> None:
    """Optional short confirmation to yourself (danpennic@gmail.com)."""
    # gmail_create_draft or gmail_send_message
    pass


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run() -> None:
    customer_id = create_customer(CUSTOMER_NAME, CUSTOMER_EMAIL)
    create_invoice_item(customer_id, AMOUNT_CENTS, ITEM_DESC)
    invoice = create_and_finalize_invoice(customer_id, DAYS_UNTIL_DUE)

    amount_display = f"${invoice['amount_due'] / 100:,.2f} {invoice['currency'].upper()}"
    draft_id = draft_customer_email(
        to=CUSTOMER_EMAIL,
        invoice_number=invoice["number"],
        amount_display=amount_display,
        hosted_url=invoice["hosted_invoice_url"],
        pdf_url=invoice["invoice_pdf"],
        personal_note=PERSONAL_NOTE,
    )

    if INTERNAL_NOTIFY:
        internal_notify(invoice)

    print("Done.")
    print(f"Customer : {customer_id}")
    print(f"Invoice  : {invoice['id']}  ({invoice['number']})")
    print(f"Status   : {invoice['status']}")
    print(f"Draft ID : {draft_id}")
    print(f"Pay link : {invoice['hosted_invoice_url']}")


if __name__ == "__main__":
    run()
