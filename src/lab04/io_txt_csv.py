from pathlib import Path
import csv
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Opens a file for reading in the specified encoding and returns its contents.
    If the file doesn't exist, a FileNotFoundError exception is thrown.
    If the specified encoding doesn't match the file's encoding,
    a UnicodeDecodeError exception is thrown.

    Example of selecting a different encoding:
    >>>content = read_text("example.txt", encoding="cp1251")
    """
    with open(path, "r", encoding=encoding) as f:
        return f.read()

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path) #Converts the given path (str or Path) to a Path object
    rows = list(rows)
    first_row_len = len(rows[0]) #Gets the length of the first line of data.
    if not all(len(row) == first_row_len for row in rows):
        raise ValueError("All data lines must be the same length.")
    # If there is a title, we check its length
    if header is not None and len(header) != first_row_len:
        raise ValueError("The header length does not match the length of the data lines.")
    with p.open("w", newline="", encoding="utf-8") as csvfile:
        w = csv.writer(csvfile)
        if header:
            w.writerow(header)
        for r in rows:
            w.writerow(r)