a = float(input("Введите размер a: "))
b = float(input("Введите размер b: "))
c = float(input("Введите размер c: "))
R = float(input("Введите радиус R: "))

d1 = (a**2 + b**2)**0.5  # Диагональ между a и b
d2 = (a**2 + c**2)**0.5  # Диагональ между a и c
d3 = (b**2 + c**2)**0.5  # Диагональ между b и c

if d1 <= 2 * R or d2 <= 2 * R or d3 <= 2 * R:
    print("Кирпич может пройти через круглое отверстие.")
else:
    print("Кирпич не может пройти через круглое отверстие.")