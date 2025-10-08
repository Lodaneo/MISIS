def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список пуст")
    if not all(isinstance(x, (int, float)) for x in nums):
        raise TypeError("Список должен содержать только числа")
    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if not all(isinstance(x, (int, float)) for x in nums):
        raise TypeError("Список должен содержать только числа")
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    flattened = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Элемент матрицы должен быть списком или кортежем")
        flattened.extend(row)
    return flattened


if __name__ == "__main__":
    print("min_max:", min_max([3, -1, 5, 5, 0]))
    print("unique_sorted:", unique_sorted([3, 1, 2, 1]))
    print("flatten:", flatten([[1, 2], (3, 4, 5)]))