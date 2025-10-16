n = int(input("Введите натуральное число n: "))

sum_cubes = 0

for i in range(1, n + 1):
    sum_cubes += i ** 3

print(f"Сумма кубов от 1^3 до {n}^3: {sum_cubes}")
