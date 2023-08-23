extensions_list = ['png', 'jpeg', 'mp3', 'aac', 'psd', 'doc', 'exe', 'txt', 'ptt',
                   'xml', 'json', 'xls', 'avi', 'gif', 'ogg', 'zip', 'rar', 'pdf']

file_name = input('Введите имя файла -> ').lower().split('.')

if len(file_name) > 1:
    cut_extension = file_name[-1]
    if cut_extension in extensions_list:
        print(f'Расширение файла - "{cut_extension}"')
    else:
        print(f'Расширение "{cut_extension}" не найдено!')