def digit_sum(value: int) -> int:
    return sum(int(digit) for digit in str(abs(value)))


def main() -> None:
    number = int(input("Введите число: "))
    if number < 0:
        print("Число должно быть неотрицательным.")
        return

    steps = 0
    while number > 0:
        number -= digit_sum(number)
        steps += 1

    print(f"Для достижения нуля потребовалось {steps} шаг(ов).")


if __name__ == "__main__":
    main()

