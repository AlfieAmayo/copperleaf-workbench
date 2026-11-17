"""Rows for demo case 1, the Ashgrove Hibiscus Lime shortage."""

PURCHASE_ORDER_ROWS = [
    {
        "po_number": "AGN-448210",
        "line_no": "1",
        "customer_id": "ASH",
        "po_date": "2026-03-02",
        "ship_to": "Ashgrove DC Edison NJ",
        "product_code": "CL-YZG-24",
        "cases_ordered": "60",
    },
    {
        "po_number": "AGN-448210",
        "line_no": "2",
        "customer_id": "ASH",
        "po_date": "2026-03-02",
        "ship_to": "Ashgrove DC Edison NJ",
        "product_code": "CL-HBL-24",
        "cases_ordered": "40",
    },
]

INVOICE_ROWS = [
    {
        "invoice_number": "CL-10482",
        "line_no": "1",
        "invoice_date": "2026-03-09",
        "customer_id": "ASH",
        "po_number": "AGN-448210",
        "product_code": "CL-YZG-24",
        "cases_billed": "60",
        "case_price_usd": "24.00",
        "line_amount_usd": "1440.00",
        "payment_terms": "NET45",
    },
    {
        "invoice_number": "CL-10482",
        "line_no": "2",
        "invoice_date": "2026-03-09",
        "customer_id": "ASH",
        "po_number": "AGN-448210",
        "product_code": "CL-HBL-24",
        "cases_billed": "40",
        "case_price_usd": "24.00",
        "line_amount_usd": "960.00",
        "payment_terms": "NET45",
    },
]

WAREHOUSE_SHIPMENT_ROWS = [
    {
        "wh_order_id": "WH-778341",
        "line_no": "1",
        "customer_po_ref": "448210",
        "destination": "ASHGROVE EDISON",
        "ship_date": "2026-03-09",
        "product_code": "CL-YZG-24",
        "cases_shipped": "60",
        "bol_number": "BOL-5521907",
    },
    {
        "wh_order_id": "WH-778341",
        "line_no": "2",
        "customer_po_ref": "448210",
        "destination": "ASHGROVE EDISON",
        "ship_date": "2026-03-09",
        "product_code": "CL-HBL-24",
        "cases_shipped": "40",
        "bol_number": "BOL-5521907",
    },
]

DELIVERY_RECEIPT_ROWS = [
    {
        "receipt_id": "RCPT-30917",
        "carrier": "Route Nine Freight",
        "bol_number": "BOL-5521907",
        "delivered_at": "2026-03-11 10:42",
        "cases_received": "100",
        "exceptions_noted": "none",
        "exception_detail": "",
        "signed_by": "Ashgrove receiving",
    },
]

ASHGROVE_REMITTANCES = {
    "AGN-PAY-0420-03": [
        {
            "remittance_date": "2026-04-20",
            "payment_id": "AGN-PAY-0420-03",
            "line_id": "1",
            "invoice_ref": "CL-10482",
            "gross_usd": "2400.00",
            "deduction_code": "02",
            "deduction_usd": "-240.00",
            "description": "SHORT 10 CS HIBISCUS",
            "net_usd": "2160.00",
        },
    ],
}
