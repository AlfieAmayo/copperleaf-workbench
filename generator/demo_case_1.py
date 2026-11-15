"""Write the source files for demo case 1, the Ashgrove Hibiscus Lime shortage."""

import csv
from pathlib import Path

OUTPUT_FOLDER = Path("generated_data")

PURCHASE_ORDER_COLUMNS = [
    "po_number",
    "line_no",
    "customer_id",
    "po_date",
    "ship_to",
    "product_code",
    "cases_ordered",
]

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

ASHGROVE_REMITTANCE_ROWS = [
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
]


def write_csv_file(
    file_path: Path, columns: list[str], rows: list[dict[str, str]]
) -> None:
    """Write a header row and data rows to a CSV file, creating its folder first."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_demo_case_1_files(output_folder: Path) -> None:
    """Write all five demo case 1 source files into the evidence folder."""
    evidence_folder = output_folder / "evidence"
    write_csv_file(
        evidence_folder / "purchase_orders.csv",
        PURCHASE_ORDER_COLUMNS,
        PURCHASE_ORDER_ROWS,
    )
    write_csv_file(
        evidence_folder / "invoices.csv",
        INVOICE_COLUMNS,
        INVOICE_ROWS,
    )
    write_csv_file(
        evidence_folder / "warehouse_shipments.csv",
        WAREHOUSE_SHIPMENT_COLUMNS,
        WAREHOUSE_SHIPMENT_ROWS,
    )
    write_csv_file(
        evidence_folder / "delivery_receipts.csv",
        DELIVERY_RECEIPT_COLUMNS,
        DELIVERY_RECEIPT_ROWS,
    )
    write_csv_file(
        evidence_folder / "remittances" / "ashgrove" / "AGN-PAY-0420-03.csv",
        ASHGROVE_REMITTANCE_COLUMNS,
        ASHGROVE_REMITTANCE_ROWS,
    )


if __name__ == "__main__":
    write_demo_case_1_files(OUTPUT_FOLDER)
