n = int(input("Введите натуральное число n: "))

sum_factorials = 0
current_factorial = 1

for i in range(1, n + 1):
    current_factorial *= i
    sum_factorials += current_factorial

print(f"Сумма факториалов от 1! до {n}! = {sum_factorials}")
