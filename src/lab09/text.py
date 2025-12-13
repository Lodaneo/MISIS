from lab08.models import Student
from lab09.group import Group
import json


g = Group("data/lab09/students.csv")


def print_students(title, students: Student):
    print("\n" + title)
    n = ""
    for s in students:
        print(f"{s.fio} || {s.birthdate} || {s.group} || {s.gpa}")
        print(f"================================================")
    


if __name__ == "__main__":
    
    print_students("Original CSV:", g.list())

    new_st = Student("Анастасия Михаил", "2004-02-22", "BIVT-08", 3.0)
    g.add(new_st)
    new_st = Student("Алекцандр Игорь", "2004-02-22", "BIVT-08", 3.0)
    g.add(new_st)
    print_students("After adding 2 students:", g.list())

    g.update("Manuel Lodaneo", gpa=4.7)

    g.find("Lodaneo")  # searching by substring

    g.remove("Manuel Lodaneo")
    
    #print(json.dumps(g.stats(), indent=5, ensure_ascii=False))
    
