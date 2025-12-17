# Задача 2: В данной действительной квадратной матрице порядка n найти
# наибольший по модулю элемент. Получить квадратную матрицу порядка n — 1
# путем отбрасывания из исходной матрицы строки и столбца, на пересечении
# которых расположен элемент с найденным значением.
# Ввод данных из файла, вывод результатов в файл.

from typing import List, Tuple


def read_matrix_from_file(filename: str) -> Tuple[int, List[List[float]]]:
    """
    Читает порядок матрицы и саму матрицу из файла.
    
    Args:
        filename: Имя файла для чтения
    
    Returns:
        Кортеж (n, matrix)
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    if len(lines) < 1:
        raise ValueError("Файл должен содержать минимум 1 строку: порядок матрицы")
    
    n = int(lines[0])
    
    if n <= 0:
        raise ValueError("Порядок матрицы должен быть положительным")
    
    if n == 1:
        raise ValueError("Матрица должна быть хотя бы 2x2 для выполнения операции")
    
    if len(lines) < 1 + n:
        raise ValueError(f"Недостаточно строк для матрицы {n}x{n}")
    
    matrix: List[List[float]] = []
    for i in range(1, 1 + n):
        row = [float(x) for x in lines[i].split()]
        if len(row) != n:
            raise ValueError(f"Строка {i} должна содержать {n} элементов")
        matrix.append(row)
    
    return n, matrix


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


def write_results_to_file(
    filename: str,
    max_element: float,
    max_row: int,
    max_col: int,
    new_matrix: List[List[float]]
) -> None:
    """
    Записывает результаты в файл.
    
    Args:
        filename: Имя файла для записи
        max_element: Наибольший по модулю элемент
        max_row: Номер строки (0-based)
        max_col: Номер столбца (0-based)
        new_matrix: Новая матрица после удаления строки и столбца
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Наибольший по модулю элемент: {max_element}\n")
        f.write(f"Позиция: строка {max_row + 1}, столбец {max_col + 1}\n")
        f.write(f"\nНовая матрица порядка {len(new_matrix)}:\n")
        for row in new_matrix:
            f.write(" ".join(f"{element:10.4f}" for element in row) + "\n")


def main() -> None:
    """Основная функция."""
    input_filename = "pasechnyiad_ym_252_vvod.txt"
    output_filename = "pasechnyiad_ym_252_vivod.txt"
    
    try:
        n, matrix = read_matrix_from_file(input_filename)
        
        max_element, max_row, max_col = find_max_abs_element(matrix)
        
        new_matrix = remove_row_and_column(matrix, max_row, max_col)
        
        write_results_to_file(output_filename, max_element, max_row, max_col, new_matrix)
        
        print(f"Результаты записаны в файл {output_filename}")
        
    except FileNotFoundError:
        print(f"Ошибка: файл {input_filename} не найден.")
    except ValueError as e:
        print(f"Ошибка в данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()

