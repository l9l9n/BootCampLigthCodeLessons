"""
Требуется определить, бьет ли слон, стоящий на клетке с указанными
координатами (номер строки и номер столбца), фигуру, стоящую на другой
указанной клетке. Вводятся четыре числа: координаты слона и координаты
другой фигуры.
"""

elefant_x = int(input("Введите номер строки для слона: "))
elefant_y = int(input("Введите номер столбца для слона: "))
figure_x = int(input("Введите номер строки для другой фигуры: "))
figure_y = int(input("Введите номер столбца для другой фигуры: "))


hit_x = abs(elefant_x - figure_x)
hit_y = abs(elefant_y - figure_y)

if hit_x == hit_y:
    print("Слон бьет фигуру!")
else:
    print("Слон не бьет фигуру!")