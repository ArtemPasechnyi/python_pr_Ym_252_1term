N = int(input("Введите количество чисел N: "))
K = int(input("Введите начальный номер K: "))

sum_fib = 0
fib1 = 1
fib2 = 1

for i in range(1, K + N):
    if i >= K:
        sum_fib += fib1
    
    fib_next = fib1 + fib2
    fib1 = fib2
    fib2 = fib_next

print(f"Сумма {N} чисел Фибоначчи начиная с {K}-го: {sum_fib}")
