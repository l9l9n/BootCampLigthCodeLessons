choice_DDR = int(input('Выберите оперативную память 4 или 8 GB: '))
choice_SSD_or_HDD = int(input('Объем памяти 256GB или 1TB: '))


if choice_DDR == 4:
    if choice_SSD_or_HDD == 256:
        print('-' * 50)
        print('Да в наличии DDR 4GB, SSD 256GB, цена: 800$')
    elif choice_SSD_or_HDD == 1:
        print('-' * 50)
        print('Да в наличии DDR 4GB, HDD 1TB, цена: 700$')
elif choice_DDR == 8:
    if choice_SSD_or_HDD == 256:
        print('-' * 50)
        print('Да в наличии DDR 8GB, SSD 256GB, цена: 950$')
    elif choice_SSD_or_HDD == 1:
        print('-' * 50)
        print('Да в наличии DDR 8GB, SSD 1TB, цена: 900$')
else:
    print('-' * 50)
    print('К сожалению такой конфигурации нету!')
print('-' * 50)
