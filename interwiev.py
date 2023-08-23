lang_programming = ['python', 'java', 'javascript']
salary = 60_000

candidate_lang_prog = input('Язык программирования: ').lower()
age = int(input('Возраст: '))
experience = int(input('Опыт: '))
desired_salary = int(input('Желаемая зарплата: '))

if candidate_lang_prog in lang_programming:
    if age >= 18 and age <= 65:
        if experience >= 3:
            if desired_salary <= salary:
                print('Подходит')
            else:
                print('Не подходит')
        else:
            print('Не подходит')
    else:
        print('Не подходит')
else:
    print('Не подходит')