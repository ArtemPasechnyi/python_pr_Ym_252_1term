print("Введите значения переменных:")
f = float(input("f = "))
v = float(input("v = "))
k = float(input("k = "))

if f < 4 and v > 6:
    S = f + v
    print(f"S = f + v = {f} + {v} = {S}")
elif v < 6:
    S = k ** 2
    print(f"S = k² = {k}² = {S}")
else:
    S = 2 * v
    print(f"S = 2v = 2 * {v} = {S}")

print(f"Результат: S = {S}")
