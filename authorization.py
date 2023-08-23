print()
print('Создайте логин и пароль!')
print('-' * 24)

user_login = [] 
user_password = []
check_login = []
check_password = []

login = input('Придумайте логин: ').lower()
password = input('Придумайте пароль: ').lower()

if login:
    if len(password) >= 8 and len(password) <= 16:
        user_login.append(login)
        user_password.append(password)

print()
print('Пожалуйста повторите логин и пароль для авторизации!')
print('-' * 53)


retry_login = input('Введите логин: ').lower()
retry_password = input('Введите пароль: ').lower()

if retry_login:
    if retry_password:
        check_login.append(retry_login)
        check_password.append(retry_password)
        if check_login == user_login:
            if check_password == user_password:
                print('True')
            else:
                print('Пароль не совпадает!')
        else:
            print('False')



# print(type(user_login), user_login)
# print(type(user_password), user_password)
# print(type(check_login), check_login)
# print(type(check_password), check_password)
