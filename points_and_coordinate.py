"""
Даны координаты двух точек на плоскости, требуется определить,
лежат ли они в одной координатной четверти или нет (все координаты
отличны от нуля). Вводятся 4 числа: координаты первой точки (x1, y1) и
координаты второй точки (x2, y2).
"""


x1 = int(input("Введите координату x1: "))
y1 = int(input("Введите координату y1: "))
x2 = int(input("Введите координату x2: "))
y2 = int(input("Введите координату y2: "))


if x1 * x2 > 0 and y1 * y2 > 0:
    print("Точки лежат в одной координатной четверти.")
else:
    print("Точки не лежат в одной координатной четверти.")