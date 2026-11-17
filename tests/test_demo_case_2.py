"""Check that demo case 2's rows appear in the files exactly as the spec shows."""

from pathlib import Path

from generator.generate import generate_all_files


def test_invoices_match_spec(tmp_path: Path) -> None:
    """The invoice file has the spec's header and contains case 2's rows."""
    generate_all_files(tmp_path)

    invoices_file = tmp_path / "evidence" / "invoices.csv"
    file_lines = invoices_file.read_text(encoding="utf-8").splitlines()

    assert file_lines[0] == (
        "invoice_number,line_no,invoice_date,customer_id,po_number,"
        "product_code,cases_billed,case_price_usd,line_amount_usd,payment_terms"
    )

    case_2_rows = [
        "CL-10540,1,2026-05-05,PEL,PWD-20877,CL-BOR-24,120,23.50,2820.00,NET45",
        "CL-10540,2,2026-05-05,PEL,PWD-20877,CL-YZG-24,40,23.50,940.00,NET45",
        "CL-10577,1,2026-05-19,PEL,PWD-20904,CL-BOR-24,80,23.50,1880.00,NET45",
        "CL-10611,1,2026-06-02,PEL,PWD-20958,CL-HBL-24,60,23.50,1410.00,NET45",
        "CL-10611,2,2026-06-02,PEL,PWD-20958,CL-CUM-24,40,23.50,940.00,NET45",
    ]
    for row in case_2_rows:
        assert row in file_lines
