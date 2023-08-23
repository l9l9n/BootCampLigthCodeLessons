cities = []

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', '{', '}',
           ']', '"', "'", '/', '|', '.', ',', '>', '<', '_', '+', '?', '=',
           '1','2','3','4','5','6','7','8','9','0']

while True:
    print('-'*35)
    print("     Выберите действие:")
    print('-'*35)
    print("1. Добавить новый город")
    print("2. Отобразить список городов")
    print("3. Заменить город")
    print("4. Удалить город")
    print("5. Выход")


    print('-'*35)
    choice = input("    Ваше действие: ")
    print('-'*35)


    if choice == "1":
        city_name = input("    Введите название города: ")
        print('-' * 35)

        if any(symbol in city_name for symbol in symbols):
            print('    Некорректное название!')
            print('-' * 35)

        elif city_name in cities:
            print(f"    Такой город уже есть! {city_name} - {cities.count(city_name)}")
            print('-' * 35)

        else:
            cities.append(city_name)
            print("    Город добавлен!")
            print('-' * 35)


    elif choice == "2":
        print("    Список городов:")
        for i, city in enumerate(cities, 1):
            print(f"{i}. {city}")

            
    elif choice == "3":
        current_city = input("Текущий город: ")
        new_city = input("Новый город: ")
        print('-' * 35)

        if current_city not in cities:
            print("Текущий город отсутствует.")
            print('-' * 35)
        elif any(symbol in new_city for symbol in symbols):
            print("Некорректное название!")
            print('-' * 35)
        elif new_city in cities:
            print(f"Такой город уже есть! {new_city} - {cities.count(new_city)}")
            print('-' * 35)
        else:
            cities[cities.index(current_city)] = new_city
            print("Город заменен.")
            print('-' * 35)


    elif choice == "4":
        city_to_remove = input("    Введите название города: ")
        
        if city_to_remove not in cities:
            print("а. Текущий город отсутствует.")
            print('-'*35)
        elif any(symbol in city_to_remove for symbol in symbols):
            print("б. Некорректное название!")
            print('-'*35)
        else:
            cities.remove(city_to_remove)
            print("в. Город удален!")
            print('-'*35)


    elif choice == "5":
        print("    Программа завершает работу")
        print('-'*35)
        break
    
    else:
        print("!!!!!!  Некорректный выбор или действие. Попробуйте снова.  !!!!!!")
