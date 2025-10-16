print("Введите три целых числа:")
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
num3 = int(input("Третье число: "))

numbers_in_range = []

if 1 <= num1 <= 3:
    numbers_in_range.append(num1)

if 1 <= num2 <= 3:
    numbers_in_range.append(num2)

if 1 <= num3 <= 3:
    numbers_in_range.append(num3)

if numbers_in_range:
    print("Числа из интервала [1,3]:", numbers_in_range)
else:
    print("Среди введенных чисел нет таких, которые принадлежат интервалу [1,3]")
