from typing import List


def read_array(name: str) -> List[int]:
    length = int(input(f"Введите количество элементов массива {name}: "))
    if length <= 0:
        raise ValueError("Размер массива должен быть положительным.")

    values: List[int] = []
    while len(values) < length:
        remaining = length - len(values)
        parts = input(
            f"Введите ещё {remaining} элемент(ов) массива {name}: "
        ).split()
        try:
            values.extend(int(part) for part in parts[:remaining])
        except ValueError:
            print("Ошибка ввода. Пожалуйста, вводите только целые числа.")
            continue
    return values


def product(values: List[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def average(values: List[int]) -> float:
    return sum(values) / len(values)


def describe_array(name: str, values: List[int]) -> None:
    prod = product(values)
    avg = average(values)
    joined_values = " ".join(str(value) for value in values)
    print(f"Массив {name}: {joined_values}")
    print(f"  Произведение элементов: {prod}")
    print(f"  Среднее арифметическое: {avg}")


def main() -> None:
    try:
        arrays = {
            "A": read_array("A"),
            "B": read_array("B"),
            "C": read_array("C"),
        }
    except ValueError as error:
        print(error)
        return

    for name, values in arrays.items():
        describe_array(name, values)


if __name__ == "__main__":
    main()

