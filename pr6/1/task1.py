from typing import List


def read_array(n: int) -> List[float]:
    values: List[float] = []
    while len(values) < n:
        remaining = n - len(values)
        parts = input(f"Введите ещё {remaining} элемент(ов) массива: ").split()
        try:
            values.extend(float(part) for part in parts[:remaining])
        except ValueError:
            print("Ошибка ввода. Пожалуйста, вводите только числа.")
            continue
    return values


def main() -> None:
    n = int(input("Введите количество элементов массива: "))
    if n <= 0:
        print("Размер массива должен быть положительным.")
        return

    numbers = read_array(n)

    min_by_abs = min(numbers, key=abs)
    print(f"Минимальный по модулю элемент: {min_by_abs}")

    reversed_numbers = " ".join(str(value) for value in reversed(numbers))
    print(f"Массив в обратном порядке: {reversed_numbers}")


if __name__ == "__main__":
    main()

