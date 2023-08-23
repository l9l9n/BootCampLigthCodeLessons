"""
Ввести координаты. Определить четверть координатной плоскости, которой принадлежит точка.
"""
while True:
    x_coord = int(input('Введите коодинату x: '))
    y_coord = int(input('Введите коодинату y: '))

    print('-'*25)

    if x_coord > 0 and y_coord > 0:
        print('Первая четверть')
    if x_coord < 0 and y_coord > 0:
        print('Вторая четверть')
    if x_coord < 0 and y_coord < 0:
        print('Третья четверть')
    if x_coord > 0 and y_coord < 0:
        print('Четвертая четверть')

    print('-'*25)


##########################################################
# Тут ниже тот же код но без цикла while

# x_coord = int(input('Введите коодинату x: '))
# y_coord = int(input('Введите коодинату y: '))

# print('-'*25)

# if x_coord > 0 and y_coord > 0:
#     print('Первая четверть')
# if x_coord < 0 and y_coord > 0:
#     print('Вторая четверть')
# if x_coord < 0 and y_coord < 0:
#     print('Третья четверть')
# if x_coord > 0 and y_coord < 0:
#     print('Четвертая четверть')
