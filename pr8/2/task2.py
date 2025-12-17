# Задача 2: В данной действительной квадратной матрице порядка n найти
# наибольший по модулю элемент. Получить квадратную матрицу порядка n — 1
# путем отбрасывания из исходной матрицы строки и столбца, на пересечении
# которых расположен элемент с найденным значением.

from typing import List, Tuple


def read_matrix(n: int) -> List[List[float]]:
    """Читает квадратную матрицу размера n x n."""
    matrix: List[List[float]] = []
    print(f"Введите элементы матрицы {n}x{n} (по строкам):")
    for i in range(n):
        row = []
        while len(row) < n:
            remaining = n - len(row)
            parts = input(f"Строка {i+1}, введите ещё {remaining} элемент(ов): ").split()
            try:
                row.extend(float(part) for part in parts[:remaining])
            except ValueError:
                print("Ошибка ввода. Пожалуйста, вводите только числа.")
                continue
        matrix.append(row)
    return matrix


def find_max_abs_element(matrix: List[List[float]]) -> Tuple[float, int, int]:
    """Находит наибольший по модулю элемент и его позицию."""
    max_abs_value = abs(matrix[0][0])
    max_row = 0
    max_col = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if abs(matrix[i][j]) > max_abs_value:
                max_abs_value = abs(matrix[i][j])
                max_row = i
                max_col = j
    
    return matrix[max_row][max_col], max_row, max_col


def remove_row_and_column(matrix: List[List[float]], row_idx: int, col_idx: int) -> List[List[float]]:
    """Удаляет строку и столбец из матрицы."""
    new_matrix = []
    for i in range(len(matrix)):
        if i != row_idx:
            new_row = []
            for j in range(len(matrix[i])):
                if j != col_idx:
                    new_row.append(matrix[i][j])
            new_matrix.append(new_row)
    return new_matrix


def print_matrix(matrix: List[List[float]]) -> None:
    """Выводит матрицу на экран."""
    for row in matrix:
        print(" ".join(f"{element:10.4f}" for element in row))


def main() -> None:
    n = int(input("Введите порядок квадратной матрицы n: "))
    if n <= 0:
        print("Порядок матрицы должен быть положительным.")
        return
    
    if n == 1:
        print("Матрица должна быть хотя бы 2x2 для выполнения операции.")
        return
    
    matrix = read_matrix(n)
    
    max_element, max_row, max_col = find_max_abs_element(matrix)
    
    print(f"\nНаибольший по модулю элемент: {max_element}")
    print(f"Позиция: строка {max_row + 1}, столбец {max_col + 1}")
    
    new_matrix = remove_row_and_column(matrix, max_row, max_col)
    
    print(f"\nНовая матрица порядка {n - 1}:")
    print_matrix(new_matrix)


if __name__ == "__main__":
    main()

