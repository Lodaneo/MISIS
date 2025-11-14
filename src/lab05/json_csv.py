import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Converts a JSON file to CSV.
    Supports a list of dictionaries [{...}, {...}], and fills missing fields with empty
    strings.
    UTF-8 encoding. Column order can be the same as in the first object or
    alphabetical (specify in the README).
    Args:
        json_path (str): Path to the input JSON file
        csv_path (str): Path to the output CSV file
    """
    J=Path(json_path) #Create objetc Path for JSON
    C=Path(csv_path) #Create object Path for CSV
    try:
        #Try: to open file JSON and read it. The info will be save on "data"
        with J.open('r', newline='', encoding='utf-8') as json_file:
            data=json.load(json_file) #Read the file, convert it in Dicty and save in "data"
            if not isinstance(data, list): #Verify if "data" is a list.
                raise ValueError("JSON data must be a list of objects")
            if not data:
                raise ValueError("JSON Cant be empty")
            headers = list(data[0].keys()) #Lets get the headers of "data" for CSV file.
        with C.open('w', newline='', encoding='utf-8') as csv_file:
            #Now lets write it on CSV file:
            #"writer" take info from "csv_file" and organize the headers
            writer=csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader() #Write the header
            writer.writerows(data) #Write rows
        print("Successfully converted JSON file to CSV file")
        print(f"Path file: {csv_path}")
        return True
    except FileNotFoundError:
        print(f"Error: File {json_path} not found")
        return False
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        return False
    except Exception as e: #Others kind of error
        print(f"Error: {e}")
        return False
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Converts CSV to JSON (list of dictionaries).
    Header is required; values ​​are stored as strings.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    data=[]
    try: #Try to: Open CVS file to read it and save the content
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader=csv.DictReader(csv_file) #Read and save as a Dicty
            for row in reader:
                converted_row={} #Our list (for) JSON
                #Loop to Write on JSON file with the respective key
                for key, value in row.items(): 
                    #Verity if "value" is a int or float or other type and convert it
                    if value.isdigit(): 
                        converted_row[key]=int(value) #convert to int if is a int type
                    else:
                        try: #try to:
                            converted_row[key]=float(value) #Convert to float if is a float type
                        except ValueError:
                            converted_row[key]=value #Just write
                data.append(converted_row) #Add new content to "data"
        if not data:
            print("Warning: CSV file is empty or has no data rows")
            return False
        #Making the conversion
        with open(json_path, 'w', encoding='utf-8') as json_file:
            #Write "data" to "json_file".Non-ASCII chars written as utf-8.
            #Identation "indent" 2 tabs
            json.dump(data, json_file, ensure_ascii=False, indent=2)
        print("Successfully converted CSV file to JSON file")
        print(f"Path file: {json_path}")
        print(f"Converted {len(data)} records")
        return True
    except FileNotFoundError:
        print(f"Error: File {csv_path} not found")
        return False
    except csv.Error as e:
        print(f"Error: CSV parsing error - {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


#Json_People="data/samples/people.json"
#JSON2CSV="data/out/people_from_json.csv"
#json_to_csv(Json_People, JSON2CSV)

CSV_People="data/samples/people.csv"
JSON_from_CSV="data/out/people_from_csv.json"
csv_to_json(CSV_People, JSON_from_CSV)