import math

x = 1.825 * (10**2)
y = 18.225
z = -3.298 * (10**-2)

print(f"Дано:")
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

try:
    y_div_x = y / x
    y_minus_x = y - x
    
    if x == 0:
        print("Ошибка: x не может быть равно нулю, деление на ноль в y/x.")
    elif y_minus_x == 0:
        print("Ошибка: (y - x) не может быть равно нулю, деление на ноль в дроби.")
    elif y_div_x < 0:
        print("Ошибка: y/x не может быть отрицательным для кубического корня.")
    else:
        term1 = abs(x**(y_div_x) - y_div_x**(1/3))
        
        numerator_term2 = math.cos(y) - z / y_minus_x

        denominator_term2 = 1 + y_minus_x**2
        
        term2 = y_minus_x * (numerator_term2 / denominator_term2)
        
        s = term1 + term2
        
        print(f"\nВычисленное значение s = {s}")
        print(f"Ожидаемый ответ: s = 1.21308")
        
        expected = 1.21308
        difference = abs(s - expected)
        print(f"Разность с ожидаемым: {difference}")
        
except Exception as e:
    print(f"Произошла ошибка при вычислении: {e}")
