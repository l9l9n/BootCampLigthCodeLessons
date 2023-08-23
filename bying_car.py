model = ['lexus', 'toyota']
colors = ["white", "grey"]
max_mileage1 = 150000
max_mileage2 = 200000
year = 2004
left_hand_drive = 'left'
max_owners = 2


input_model = input('Model: ').lower()
input_mileage = int(input('Miliage: '))
input_year = int(input('Year: '))
input_color = input('Color: ').lower()
input_owners = int(input('Owners: '))
input_hand_drive = input('Hand drive: ').lower()

if input_model in model:
    if input_mileage <= max_mileage1:
        if input_year == year:
            if input_color in colors:
                if input_owners <= max_owners:
                    if input_hand_drive == left_hand_drive:
                        print('-' * 70)
                        print(f'Option 1:\n'
                              f'Model: {input_model}\n'
                              f'Mileage: {input_mileage}\n'
                              f'Year: {input_year}\n'
                              f'Color: {input_color}\n'
                              f'Owners: {input_owners}\n'
                              f'Hand drive: {input_hand_drive}\n'
                                '-- price : 10000$ --\n')
                    else:
                        print('-' * 70)
                        print('Sorry not option')
                else:
                    print('-' * 70)
                    print('Sorry not option')
            else:
                print('-' * 70)
                print('Sorry not option')
        else:
            print('-' * 70)
            print('Sorry not option')

    elif input_mileage <= max_mileage2 and input_mileage >= max_mileage1:
        if input_year == year:
            if input_color in colors:
                if input_owners <= max_owners:
                    if input_hand_drive == left_hand_drive:
                        print('-'*70)
                        print(f'Option 2:\n'
                              f'Model: {input_model}\n'
                              f'Mileage: {input_mileage}\n'
                              f'Year: {input_year}\n'
                              f'Color: {input_color}\n'
                              f'Owners: {input_owners}\n'
                              f'Hand drive: {input_hand_drive}\n'
                                '-- price : 8000$ --\n')
                    else:
                        print('-' * 70)
                        print('Sorry not option')
                else:
                    print('-' * 70)
                    print('Sorry not option')
            else:
                print('-' * 70)
                print('Sorry not option')
        else:
            print('-' * 70)
            print('Sorry not option')
else:
    print('-' * 70)
    print('Sorry not option')
    