# src/lab02/tuples.py

def format_record(rec: tuple[str, str, float]) -> str:
    """
    Форматирует запись студента.
    Вход: (ФИО, группа, GPA)
    Выход: 'Иванов И.И., гр. BIVT-25, GPA 4.60'
    """
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("Ожидается кортеж (fio, group, gpa)")

    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("fio и group должны быть строками")
    if not isinstance(gpa, (int, float)):
        raise TypeError("gpa должен быть числом")

    fio = " ".join(fio.strip().split())  # убираем лишние пробелы
    if not fio or not group.strip():
        raise ValueError("fio и group не могут быть пустыми")

    parts = fio.split()
    if len(parts) < 2:
        raise ValueError("ФИО должно содержать минимум фамилию и имя")

    surname = parts[0].capitalize()
    initials = "".join(p[0].upper() + "." for p in parts[1:3])  # 1–2 инициалов

    return f"{surname} {initials}, гр. {group.strip()}, GPA {gpa:.2f}"


# Примеры запуска
if __name__ == "__main__":
    print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
    print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))