"""Check that demo case 1's rows appear in the files exactly as the spec shows."""

from pathlib import Path

from generator.generate import generate_all_files


def test_purchase_orders_match_spec(tmp_path: Path) -> None:
    """The purchase order file has the spec's header and contains case 1's rows."""
    generate_all_files(tmp_path)

    purchase_orders_file = tmp_path / "evidence" / "purchase_orders.csv"
    file_lines = purchase_orders_file.read_text(encoding="utf-8").splitlines()

    assert file_lines[0] == (
        "po_number,line_no,customer_id,po_date,ship_to,product_code,cases_ordered"
    )

    case_1_rows = [
        "AGN-448210,1,ASH,2026-03-02,Ashgrove DC Edison NJ,CL-YZG-24,60",
        "AGN-448210,2,ASH,2026-03-02,Ashgrove DC Edison NJ,CL-HBL-24,40",
    ]
    for row in case_1_rows:
        assert row in file_lines


def test_invoices_match_spec(tmp_path: Path) -> None:
    """The invoice file has the spec's header and contains case 1's rows."""
    generate_all_files(tmp_path)

    invoices_file = tmp_path / "evidence" / "invoices.csv"
    file_lines = invoices_file.read_text(encoding="utf-8").splitlines()

    assert file_lines[0] == (
        "invoice_number,line_no,invoice_date,customer_id,po_number,"
        "product_code,cases_billed,case_price_usd,line_amount_usd,payment_terms"
    )

    case_1_rows = [
        "CL-10482,1,2026-03-09,ASH,AGN-448210,CL-YZG-24,60,24.00,1440.00,NET45",
        "CL-10482,2,2026-03-09,ASH,AGN-448210,CL-HBL-24,40,24.00,960.00,NET45",
    ]
    for row in case_1_rows:
        assert row in file_lines


def test_warehouse_shipments_match_spec(tmp_path: Path) -> None:
    """The warehouse shipments file has the spec's header and contains case 1's rows."""
    generate_all_files(tmp_path)

    warehouse_shipments_file = tmp_path / "evidence" / "warehouse_shipments.csv"
    file_lines = warehouse_shipments_file.read_text(encoding="utf-8").splitlines()

    assert file_lines[0] == (
        "wh_order_id,line_no,customer_po_ref,destination,ship_date,"
        "product_code,cases_shipped,bol_number"
    )

    case_1_rows = [
        "WH-778341,1,448210,ASHGROVE EDISON,2026-03-09,CL-YZG-24,60,BOL-5521907",
        "WH-778341,2,448210,ASHGROVE EDISON,2026-03-09,CL-HBL-24,40,BOL-5521907",
    ]
    for row in case_1_rows:
        assert row in file_lines


def test_delivery_receipts_match_spec(tmp_path: Path) -> None:
    """The delivery receipts file has the spec's header and contains case 1's rows."""
    generate_all_files(tmp_path)

    delivery_receipts_file = tmp_path / "evidence" / "delivery_receipts.csv"
    file_lines = delivery_receipts_file.read_text(encoding="utf-8").splitlines()

    assert file_lines[0] == (
        "receipt_id,carrier,bol_number,delivered_at,"
        "cases_received,exceptions_noted,exception_detail,signed_by"
    )

    case_1_rows = [
        "RCPT-30917,Route Nine Freight,BOL-5521907,"
        "2026-03-11 10:42,100,none,,Ashgrove receiving",
    ]
    for row in case_1_rows:
        assert row in file_lines


def test_ashgrove_remittance_matches_spec(tmp_path: Path) -> None:
    """The Ashgrove remittance file matches the spec line for line."""
    generate_all_files(tmp_path)

    file_text = (
        tmp_path / "evidence" / "remittances" / "ashgrove" / "AGN-PAY-0420-03.csv"
    ).read_text(encoding="utf-8")

    assert file_text == (
        "remittance_date,payment_id,line_id,invoice_ref,"
        "gross_usd,deduction_code,deduction_usd,description,net_usd\n"
        "2026-04-20,AGN-PAY-0420-03,1,CL-10482,2400.00,"
        "02,-240.00,SHORT 10 CS HIBISCUS,2160.00\n"
    )
