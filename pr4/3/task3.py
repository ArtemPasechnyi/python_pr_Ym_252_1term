


A = int(input("Введите число A: "))
B = int(input("Введите число B: "))


if A > B:

    for i in range(A, B - 1, -1):
        if i % 2 == 1:
            print(i)
else:
    print("Ошибка: A должно быть больше B")