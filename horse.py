"""
Требуется определить, бьет ли конь, стоящий на клетке с указанными координатами 
(номер строки и номер столбца), фигуру, стоящую на другой указанной клетке. 
Вводятся четыре числа: координаты коня и координаты другой фигуры.
"""


horse_x = int(input("Введите координату x для коня: "))
horse_y = int(input("Введите координату y для коня: "))
figure_x = int(input("Введите координату x для другой фигуры: "))
figure_y = int(input("Введите координату y для другой фигуры: "))


hit_x = abs(horse_x - figure_x)
hit_y = abs(horse_y - figure_y)

# print(hit_x)
# print(hit_y)

if hit_x == 1 and hit_y == 2 or hit_x == 2 and hit_y == 1:
    print("Конь бьет фигуру!")
else:
    print("Конь не бьет фигуру!")
    