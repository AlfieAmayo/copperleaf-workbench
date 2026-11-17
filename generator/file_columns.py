"""Column names for each type of data file, in the order the spec lists them."""

PRODUCT_COLUMNS = [
    "product_code",
    "product_name",
    "case_pack",
    "can_size_fl_oz",
    "standard_case_price_usd",
]

PRICE_LIST_COLUMNS = [
    "customer_id",
    "product_code",
    "effective_from",
    "effective_to",
    "case_price_usd",
]

PURCHASE_ORDER_COLUMNS = [
    "po_number",
    "line_no",
    "customer_id",
    "po_date",
    "ship_to",
    "product_code",
    "cases_ordered",
]

INVOICE_COLUMNS = [
    "invoice_number",
    "line_no",
    "invoice_date",
    "customer_id",
    "po_number",
    "product_code",
    "cases_billed",
    "case_price_usd",
    "line_amount_usd",
    "payment_terms",
]

WAREHOUSE_SHIPMENT_COLUMNS = [
    "wh_order_id",
    "line_no",
    "customer_po_ref",
    "destination",
    "ship_date",
    "product_code",
    "cases_shipped",
    "bol_number",
]

DELIVERY_RECEIPT_COLUMNS = [
    "receipt_id",
    "carrier",
    "bol_number",
    "delivered_at",
    "cases_received",
    "exceptions_noted",
    "exception_detail",
    "signed_by",
]

ASHGROVE_REMITTANCE_COLUMNS = [
    "remittance_date",
    "payment_id",
    "line_id",
    "invoice_ref",
    "gross_usd",
    "deduction_code",
    "deduction_usd",
    "description",
    "net_usd",
]
