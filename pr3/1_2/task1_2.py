number = int(input("Введите двузначное число: "))

first_digit = number // 10
second_digit = number % 10

if first_digit == second_digit:
    print("Да")
else:
    print("Нет")
