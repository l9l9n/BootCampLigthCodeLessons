districts = ['чон арык', 'байтик', 'ортосай']
blok = ['кирпич', 'кирпичный', 'кирпича']
sand_blok = ['пескоблок', 'пескоблока']

input_district = input('Выберите район Чон Арык, Байтик или Ортосай: ').lower()
input_material = input('Дом кирпичный или из пескоблока: ').lower()
input_plot = int(input('Размер участка: '))


if input_district in districts:
    if input_material in blok:
        if input_plot == 4:
            print('-'* 60)
            print(f'Вариант 1:\n'
                  f'Район: {input_district}\n'
                  f"Материал дома: {input_material}\n"
                  f'Площадь участка: {input_plot} соток\n'
                  f'Cтоимость: 50 000\n')
        else:
            print('Нет вариатов')

    elif input_material in sand_blok:
        if input_plot == 5:
            print('-' * 60)
            print(f'Вариант 2:\n'
                  f'Район: {input_district}\n'
                  f"Материал дома: {input_material}\n"
                  f'Площадь участка: {input_plot} соток\n'
                  f'Cтоимость: 45 000\n')
        else:
            print('Нет вариатов')
else:
    print(f'Района с названием {input_district} не существует!')

