"""Check that the reference files every case relies on match the spec exactly."""

from pathlib import Path

import yaml

from generator.generate import generate_all_files


def test_products_match_spec(tmp_path: Path) -> None:
    """The products file matches the spec line for line."""
    generate_all_files(tmp_path)

    file_text = (tmp_path / "evidence" / "products.csv").read_text(encoding="utf-8")

    assert file_text == (
        "product_code,product_name,case_pack,"
        "can_size_fl_oz,standard_case_price_usd\n"
        "CL-YZG-24,Yuzu Ginger,24,12,26.00\n"
        "CL-HBL-24,Hibiscus Lime,24,12,26.00\n"
        "CL-BOR-24,Blood Orange,24,12,26.00\n"
        "CL-CUM-24,Cucumber Mint,24,12,26.00\n"
    )


def test_price_list_matches_spec(tmp_path: Path) -> None:
    """The price list file matches the spec line for line."""
    generate_all_files(tmp_path)

    file_text = (tmp_path / "evidence" / "price_list.csv").read_text(encoding="utf-8")

    assert file_text == (
        "customer_id,product_code,effective_from,effective_to,case_price_usd\n"
        "ASH,CL-YZG-24,2026-01-01,,24.00\n"
        "ASH,CL-HBL-24,2026-01-01,,24.00\n"
        "ASH,CL-BOR-24,2026-01-01,,24.00\n"
        "ASH,CL-CUM-24,2026-01-01,,24.00\n"
        "PEL,CL-YZG-24,2026-01-01,,23.50\n"
        "PEL,CL-HBL-24,2026-01-01,,23.50\n"
        "PEL,CL-BOR-24,2026-01-01,,23.50\n"
        "PEL,CL-CUM-24,2026-01-01,,23.50\n"
    )


def test_customer_policies_keep_codes_as_text(tmp_path: Path) -> None:
    """Deduction codes stay text, so the shortage code keeps its leading zero."""
    generate_all_files(tmp_path)

    policies_file = tmp_path / "configuration" / "customer_policies.yaml"
    policies = yaml.safe_load(policies_file.read_text(encoding="utf-8"))

    assert policies["ASH"]["deduction_codes"]["shortage"] == "02"
    assert policies["PEL"]["deduction_codes"]["shortage"] == "SH"
