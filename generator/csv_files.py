"""Write CSV files exactly as the spec prints them."""

import csv
from pathlib import Path


def write_csv_file(
    file_path: Path, columns: list[str], rows: list[dict[str, str]]
) -> None:
    """Write a header row and data rows to a CSV file, creating its folder first."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
