while True:
    print()
    word = input('Введите слово: ').lower()
    revers = word[::-1]

    if word == revers:
        print(f'Cлово "{word}" является палиндром.')
    else:
        print(f'Cлово "{word}" не является палиндром.')
