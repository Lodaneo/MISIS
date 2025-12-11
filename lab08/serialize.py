import json
from src.lab08.models import Student
from pathlib import Path


def students_to_json(students: list[Student], path: str):
    """
    Serializes datas into a JSON file.
    """
    Json_path = Path(path)
    # Certify that its a .JSON file
    if Json_path.suffix.lower() != ".json":
        print(f"The file is not of the .json type.")
        return False
    # Creates the serialization to write the serialized data to the JSON file.
    data_to_JSON = [s.to_dict() for s in students]
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data_to_JSON, f, ensure_ascii=False, indent=2)
        print(f"Data successfully saved to '{path}'.")
    except ValueError as e:
        print(f"Error writing to file {path}: {e}")


def students_from_json(path) -> list[Student]:
    """
    Disserializes datas from a JSON file.
    """
    Json_path = Path(path)
    if Json_path.suffix.lower() != ".json":
        print(f"The file is not of the .json type.")
        return False
    try:
        with open(path, "r", encoding="utf-8") as f:
            data_from_json = json.load(f)
        if not isinstance(data_from_json, list):
            raise TypeError("Expected JSON list/array, but got a diferent type")
        students = []  # Creates a new empty list
        for item in data_from_json:
            try:
                # Disserialize the items in "data_from_json" and Save to the list.
                students.append(Student.from_dict(item))
            except:
                raise ValueError(f"Error processing student data from JSON: {item}")
        return students
    except:
        raise ValueError("Error: File Not Found!!!")


# --------Runing funcions--------
if __name__ == "__main__":
    students_list = [
        Student("André Pedro João", "2003-05-15", "БИВТ-6", 4.2),
        Student("Lodánio Nkoko Manuel", "2007-11-30", "A-50", 4.0),
        Student("Francisco Filho", "1998-11-30", "M-6", 4.2),
    ]
    students_to_json(students_list, "data/lab08/students_output.json")
    loaded_students = students_from_json("data/lab08/students_input.json")
    print("Disserialized data (str):\n")
    for items in loaded_students:
        print(items)