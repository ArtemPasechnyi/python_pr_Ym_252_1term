import math

print("Введите длины сторон треугольника:")
a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    print(f"Полупериметр треугольника: {p}")
    print(f"Площадь треугольника: {area:.2f}")
else:
    print("Ошибка: Треугольник с такими сторонами не существует!")
    print("Сумма любых двух сторон должна быть больше третьей стороны.")
