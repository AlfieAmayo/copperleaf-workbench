"""Collect every case's rows and write each data file once into generated_data."""

from pathlib import Path

from generator import demo_case_1, file_columns, reference_data
from generator.csv_files import write_csv_file

OUTPUT_FOLDER = Path("generated_data")


def write_evidence_files(output_folder: Path) -> None:
    """Write one evidence file per type of paperwork, holding every case's rows."""
    evidence_folder = output_folder / "evidence"
    write_csv_file(
        evidence_folder / "products.csv",
        file_columns.PRODUCT_COLUMNS,
        reference_data.PRODUCT_ROWS,
    )
    write_csv_file(
        evidence_folder / "purchase_orders.csv",
        file_columns.PURCHASE_ORDER_COLUMNS,
        demo_case_1.PURCHASE_ORDER_ROWS,
    )
    write_csv_file(
        evidence_folder / "invoices.csv",
        file_columns.INVOICE_COLUMNS,
        demo_case_1.INVOICE_ROWS,
    )
    write_csv_file(
        evidence_folder / "warehouse_shipments.csv",
        file_columns.WAREHOUSE_SHIPMENT_COLUMNS,
        demo_case_1.WAREHOUSE_SHIPMENT_ROWS,
    )
    write_csv_file(
        evidence_folder / "delivery_receipts.csv",
        file_columns.DELIVERY_RECEIPT_COLUMNS,
        demo_case_1.DELIVERY_RECEIPT_ROWS,
    )


def write_ashgrove_remittances(output_folder: Path) -> None:
    """Write one remittance file per Ashgrove payment, named by its payment ID."""
    remittance_folder = output_folder / "evidence" / "remittances" / "ashgrove"
    for payment_id, rows in demo_case_1.ASHGROVE_REMITTANCES.items():
        write_csv_file(
            remittance_folder / f"{payment_id}.csv",
            file_columns.ASHGROVE_REMITTANCE_COLUMNS,
            rows,
        )


def generate_all_files(output_folder: Path) -> None:
    """Write every data file the generator makes."""
    write_evidence_files(output_folder)
    write_ashgrove_remittances(output_folder)


if __name__ == "__main__":
    generate_all_files(OUTPUT_FOLDER)
