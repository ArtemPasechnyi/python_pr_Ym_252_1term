N = int(input("Введите количество чисел N: "))

if N == 1:
    sum_fib = 1
elif N == 2:
    sum_fib = 2
else:
    fib1 = 1
    fib2 = 1
    sum_fib = 2 
    
    for i in range(3, N + 1):
        fib_next = fib1 + fib2
        sum_fib += fib_next
        fib1 = fib2
        fib2 = fib_next

print(f"Сумма первых {N} чисел Фибоначчи: {sum_fib}")
