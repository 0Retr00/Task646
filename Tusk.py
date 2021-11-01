documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
def get_name():
    number = input('Введите номер документа:  ')
    for data in documents:
        if data.get("number") == number:
            return data.get('name')
    return 'Документа с таким номером нет'
 
def shelf_number(arg_number):
    shelf_break = False
    for shelf_directory in directories.items():
        for doc_number in shelf_directory[1]:
            if doc_number == arg_number:
                print('Данный документ находится на полке - ', shelf_directory[0])
                shelf_break = True
                break
        if shelf_break == True:
            break
    else:
        print('  Внимание! Документа нет на полке.')
 
def get_list():
    for document in documents:
        print('{} "{}" "{}"'.format(document['type'], document['number'], document['name']))
 
 
def add_new_document(agr_type, arg_number, arg_name, arg_dir_number):
    if int(arg_dir_number) == 1 or int(arg_dir_number) == 2 or int(arg_dir_number) == 3:
        documents.append({"type": agr_type, "number": arg_number, "name": arg_name})
        directories[arg_dir_number].append(arg_number)
        print('\n  Ваш документ добавлен в Архив!')
    else:
        print('\n  Внимание! Такой полки не существует.')
    
 
 
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
 
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
 
while True:
    print('Возможные команды: p, s, l, a')
    comand = input('Введите название команды ')
 
    if comand == 'p':
        print(get_name())
    
    elif comand == 's':
            shelf_number(input('\nВведите номер документа:'))
    
    elif comand == 'l':
        print(get_list())
    
    elif comand == 'a':
       add_new_document(input('\nВведите тип документа (passport,invoice,insurance...):'),
                         input('Введите номер документа: '), input('Введите имя: '),
                         input('Введите номер полки (1, 2, 3): '))
       print (documents)
    else:
             print('Вы ввели команду не корректно, повторите ввод.')

