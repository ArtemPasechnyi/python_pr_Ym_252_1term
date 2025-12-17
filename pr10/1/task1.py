# Задача 1: Для целочисленной квадратной матрицы найти число элементов,
# кратных k, и наибольший из этих элементов.
# Ввод данных из файла, вывод результатов в файл.

from typing import List, Optional, Tuple


def read_matrix_from_file(filename: str) -> Tuple[int, int, List[List[int]]]:
    """
    Читает размер матрицы, число k и саму матрицу из файла.
    
    Args:
        filename: Имя файла для чтения
    
    Returns:
        Кортеж (n, k, matrix)
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    if len(lines) < 2:
        raise ValueError("Файл должен содержать минимум 2 строки: размер матрицы и число k")
    
    n = int(lines[0])
    k = int(lines[1])
    
    if n <= 0:
        raise ValueError("Размер матрицы должен быть положительным")
    
    if k == 0:
        raise ValueError("k не может быть равно нулю")
    
    if len(lines) < 2 + n:
        raise ValueError(f"Недостаточно строк для матрицы {n}x{n}")
    
    matrix: List[List[int]] = []
    for i in range(2, 2 + n):
        row = [int(x) for x in lines[i].split()]
        if len(row) != n:
            raise ValueError(f"Строка {i-1} должна содержать {n} элементов")
        matrix.append(row)
    
    return n, k, matrix


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


def write_results_to_file(filename: str, k: int, count: int, max_element: Optional[int]) -> None:
    """
    Записывает результаты в файл.
    
    Args:
        filename: Имя файла для записи
        k: Число для проверки кратности
        count: Количество элементов, кратных k
        max_element: Наибольший элемент, кратный k
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Количество элементов, кратных {k}: {count}\n")
        if max_element is not None:
            f.write(f"Наибольший элемент, кратный {k}: {max_element}\n")
        else:
            f.write(f"Элементов, кратных {k}, не найдено.\n")


def main() -> None:
    """Основная функция."""
    input_filename = "pasechnyiad_ym_252_vvod.txt"
    output_filename = "pasechnyiad_ym_252_vivod.txt"
    
    try:
        n, k, matrix = read_matrix_from_file(input_filename)
        
        count, max_element = find_multiples_and_max(matrix, k)
        
        write_results_to_file(output_filename, k, count, max_element)
        
        print(f"Результаты записаны в файл {output_filename}")
        
    except FileNotFoundError:
        print(f"Ошибка: файл {input_filename} не найден.")
    except ValueError as e:
        print(f"Ошибка в данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()

