from typing import List


ARRAY_SIZE = 10


def read_array(name: str) -> List[float]:
    values: List[float] = []
    while len(values) < ARRAY_SIZE:
        remaining = ARRAY_SIZE - len(values)
        parts = input(
            f"Введите ещё {remaining} элемент(ов) массива {name}: "
        ).split()
        try:
            values.extend(float(part) for part in parts[:remaining])
        except ValueError:
            print("Ошибка ввода. Пожалуйста, вводите только числа.")
            continue
    return values


def format_array(values: List[float]) -> str:
    return " ".join(str(value) for value in values)


def main() -> None:
    array_a = read_array("A")
    array_b = read_array("B")

    print(f"Исходный массив A: {format_array(array_a)}")
    print(f"Исходный массив B: {format_array(array_b)}")

    for i in range(ARRAY_SIZE):
        array_a[i], array_b[i] = array_b[i], array_a[i]

    print(f"Преобразованный массив A: {format_array(array_a)}")
    print(f"Преобразованный массив B: {format_array(array_b)}")


if __name__ == "__main__":
    main()

