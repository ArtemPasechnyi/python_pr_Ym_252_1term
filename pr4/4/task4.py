N = int(input("Введите количество чисел N: "))

sum = 0

for i in range(N):
    sum += int(input(f"Введите {i+1}-е число: "))

print(f"Сумма чисел: {sum}")
