# src/lab02/matrix.py

def check_rectangular(mat: list[list]) -> None:
    """Проверяет, что матрица прямоугольная (все строки одинаковой длины)."""
    if not mat:
        return
    row_len = len(mat[0])
    if any(len(row) != row_len for row in mat):
        raise ValueError("Матрица не прямоугольная")


def transpose(mat: list[list[float | int]]) -> list[list]:
    """
    Транспонирует матрицу (меняет строки и столбцы местами).
    Пустая матрица → [].
    """
    if not mat:
        return []

    check_rectangular(mat)
    return [list(row) for row in zip(*mat)]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает список сумм по строкам."""
    if not mat:
        return []

    check_rectangular(mat)
    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает список сумм по столбцам."""
    if not mat:
        return []

    check_rectangular(mat)
    return [sum(col) for col in zip(*mat)]


# Примеры запуска
if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    print("transpose:", transpose(m))  # [[1, 4], [2, 5], [3, 6]]
    print("row_sums:", row_sums(m))    # [6, 15]
    print("col_sums:", col_sums(m))    # [5, 7, 9]