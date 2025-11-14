import csv
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Converts CSV to XLSX.
    Use openpyxl or xlsxwriter.
    The first row of the CSV is the header.
    The sheet is called "Sheet1."
    Columns are auto-widthed to fit the text length (at least 8 characters).
    """
    try:
        # Crie um novo workbook e pegue a planilha ativa
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # Abra o arquivo CSV e leia o conteúdo
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                # Adicione cada linha do CSV à planilha
                ws.append(row)

        # save o workbook como um arquivo XLSX
        wb.save(xlsx_path)
        print("Successfully converted CSV file to XLSX using openpyxl python module.")
        print(f"Path file: {xlsx_path}")

    except FileNotFoundError:
        print(f"Error: CSV File '{csv_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

CSV_Cities="data/samples/cities.csv"
XLSX_from_CSV="data/out/cities.xlsx"
csv_to_xlsx(CSV_Cities, XLSX_from_CSV)