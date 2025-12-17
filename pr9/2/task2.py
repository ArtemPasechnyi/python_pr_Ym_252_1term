# Задача 2: Дана последовательность натуральных чисел (одно число в строке),
# завершающаяся числом 0. Определите значение второго по величине элемента
# в этой последовательности, то есть элемента, который будет наибольшим,
# если из последовательности удалить наибольший элемент.
# Решение с помощью рекурсии.

from typing import Optional, Tuple


def find_second_largest_recursive(
    max_val: Optional[int] = None,
    second_max: Optional[int] = None
) -> Optional[int]:
    """
    Рекурсивно находит второй по величине элемент в последовательности.
    
    Args:
        max_val: Текущее максимальное значение
        second_max: Текущее второе по величине значение
    
    Returns:
        Второе по величине значение или None, если его нет
    """
    try:
        num = int(input())
        
        # Если встретили 0, завершаем рекурсию
        if num == 0:
            return second_max
        
        # Если число не натуральное, пропускаем его
        if num <= 0:
            return find_second_largest_recursive(max_val, second_max)
        
        # Первое натуральное число
        if max_val is None:
            return find_second_largest_recursive(num, None)
        
        # Обновляем максимум и второй максимум
        if num > max_val:
            # Новое число больше текущего максимума
            return find_second_largest_recursive(num, max_val)
        elif num == max_val:
            # Число равно максимуму, второй максимум не меняется
            return find_second_largest_recursive(max_val, second_max)
        else:
            # Число меньше максимума
            if second_max is None or num > second_max:
                # Обновляем второй максимум
                return find_second_largest_recursive(max_val, num)
            else:
                # Второй максимум не меняется
                return find_second_largest_recursive(max_val, second_max)
    
    except ValueError:
        print("Ошибка ввода. Пожалуйста, вводите только целые числа.")
        return find_second_largest_recursive(max_val, second_max)


def main() -> None:
    """Основная функция для нахождения второго по величине элемента."""
    print("Введите последовательность натуральных чисел (одно число в строке).")
    print("Для завершения введите 0:")
    
    result = find_second_largest_recursive()
    
    if result is not None:
        print(f"\nВторой по величине элемент: {result}")
    else:
        print("\nВ последовательности недостаточно элементов для определения второго по величине.")


if __name__ == "__main__":
    main()

