# Задача 1: Для целочисленной квадратной матрицы найти число элементов,
# кратных k, и наибольший из этих элементов.

from typing import List, Optional, Tuple


def read_matrix(n: int) -> List[List[int]]:
    """Читает квадратную матрицу размера n x n."""
    matrix: List[List[int]] = []
    print(f"Введите элементы матрицы {n}x{n} (по строкам):")
    for i in range(n):
        row = []
        while len(row) < n:
            remaining = n - len(row)
            parts = input(f"Строка {i+1}, введите ещё {remaining} элемент(ов): ").split()
            try:
                row.extend(int(part) for part in parts[:remaining])
            except ValueError:
                print("Ошибка ввода. Пожалуйста, вводите только целые числа.")
                continue
        matrix.append(row)
    return matrix


def find_multiples_and_max(matrix: List[List[int]], k: int) -> Tuple[int, Optional[int]]:
    """Находит количество элементов, кратных k, и наибольший из них."""
    multiples = []
    for row in matrix:
        for element in row:
            if element % k == 0:
                multiples.append(element)
    
    count = len(multiples)
    max_element = max(multiples) if multiples else None
    return count, max_element


def main() -> None:
    n = int(input("Введите размер квадратной матрицы n: "))
    if n <= 0:
        print("Размер матрицы должен быть положительным.")
        return
    
    k = int(input("Введите число k: "))
    if k == 0:
        print("k не может быть равно нулю.")
        return
    
    matrix = read_matrix(n)
    
    count, max_element = find_multiples_and_max(matrix, k)
    
    print(f"\nКоличество элементов, кратных {k}: {count}")
    if max_element is not None:
        print(f"Наибольший элемент, кратный {k}: {max_element}")
    else:
        print(f"Элементов, кратных {k}, не найдено.")


if __name__ == "__main__":
    main()

