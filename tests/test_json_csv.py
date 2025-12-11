import pytest
from pathlib import Path
import json
import csv
from lab05.json_csv import json_to_csv, csv_to_json


# ---------------------------------------------------------------#
# -------------------TESTES JSON2CSV----------------------------#
# ---------------------------------------------------------------#
def test_json_to_csv_path_validation(tmp_path: Path):
    """Validate the JSON path. File MUST be a .json file"""
    src = tmp_path / "people"
    dst = tmp_path / "people.csv"
    # with pytest.raises(ValueError):
    #   json_to_csv(str(src), str(dst))
    assert json_to_csv(str(src), str(dst)) is False


# ---------------------------------------------------------------#
def test_json_to_csv_wrong_header(tmp_path: Path):
    """Validate the JSON file HEADER - HEADER MUST BE "name" and "age" """
    src = tmp_path / "WRONG_HEADER.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": -5},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    # with pytest.raises(ValueError):
    #    json_to_csv(str(src), str(dst))
    assert json_to_csv(str(src), str(dst)) is False


# ---------------------------------------------------------------#
def test_json_to_csv_empty_file(tmp_path: Path):
    """Validate the JSON file content - file CAN NOT BE empty"""
    src = tmp_path / "emptyfile.json"
    dst = tmp_path / "people.csv"
    data = []
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    # with pytest.raises(ValueError):
    #    json_to_csv(str(src), str(dst))
    assert json_to_csv(str(src), str(dst)) is False


# ---------------------------------------------------------------#
def test_json_to_csv_roundtrip(tmp_path: Path):
    """Test converting CSV data to JSON format."""
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]
    # Write "data" in file people.json
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))  # Now convert it to CSV

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))  # get wht is written on new json file

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())  # Verify if there are the headers


# ---------------------------------------------------------------#
# -------------------TESTES CSV2JSON----------------------------#
# ---------------------------------------------------------------#
def test_csv_to_json_path_validation(tmp_path: Path):
    """Validate the CSV path. File MUST be a .csv file"""
    src = tmp_path / "people"
    dst = tmp_path / "people.json"
    data = [
        {"name": "Alice", "age": 22},
    ]
    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(data)
    # with pytest.raises(ValueError):
    #   csv_to_json(str(src), str(dst))
    assert csv_to_json(str(src), str(dst)) is False


# ---------------------------------------------------------------#
def test_csv_to_json_wrong_header(tmp_path: Path):
    """Validate the CSV file HEADER - HEADER MUST BE "name" and "age" """
    src = tmp_path / "WRONG_HEADER.csv"
    dst = tmp_path / "people.json"
    data = [
        {"NAME": "Alice", "AGE": 22},
    ]
    src.touch()  # Just open and close the file
    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["NAME", "AGE"])
        writer.writeheader()
        writer.writerows(data)
    # with pytest.raises(ValueError):
    #    csv_to_json(str(src), str(dst))
    assert csv_to_json(str(src), str(dst)) is False


# ---------------------------------------------------------------#
def test_csv_to_json_empty_file(tmp_path: Path):
    """Validate the CSV file content - file CAN NOT BE empty"""
    src = tmp_path / "emptyfile.csv"
    dst = tmp_path / "people.json"
    src.touch()  # Just open and close the file
    # with pytest.raises(ValueError):
    # csv_to_json(str(src), str(dst))
    assert csv_to_json(str(src), str(dst)) is False


# ---------------------------------------------------------------#
def test_csv_to_json_roundtrip(tmp_path: Path):
    """Test converting CSV data to JSON format."""
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(data)
    assert csv_to_json(str(src), str(dst)) is True
    # Read the output JSON and assert its contents
    assert dst.exists()
    with dst.open(encoding="utf-8") as f:
        output_data = json.load(f)
    assert len(output_data) == 2
    # When converting back to JSON, it should match the original list of dictionaries
    assert {"name", "age"} <= set(output_data[0].keys())
