from tabulate import tabulate

def addData():
    file = open('contacts.txt', 'a', encoding='UTF-16')
    first_name = input('\nВведите имя: ')
    second_name = input('Введите фамилию: ')
    mid_name = input('Введите отчество: ')
    number = input('Введите номер телефона: ')
    item = [first_name, second_name, mid_name, number]
    file.writelines('.'.join(item))
    file.writelines(';')
    file.close()

def printData():
    file = open('contacts.txt', 'r', encoding='UTF-16')
    print()
    for line in file:
        item = line.split(';')
        data = []
        for i in item:
            if i != '':
                data.append(i.split('.'))
        head = ['Имя', 'Фамилия', 'Отчество', 'Номер телефона']
        print(tabulate(data, headers=head, tablefmt="grid"))
        input("Нажмите Enter для продолжения...")
    file.close()

def SearchData():
    file = open('contacts.txt', 'r', encoding='UTF-16')
    strSearch = input('\nВведите информацию для поиска контакта (имя, фамилию, отчество, номер телефона): ').lower()
    for line in file:
        item = line.split(';')
        data = []
        for i in item:
            if i != '' and strSearch in i.lower():
                data.append(i.split('.'))
        if data == []:
            if input('\nТакой информации в справочнике нет. Вывести все контакты? (Да/Нет) ').lower() == 'да':
                printData()
            else: break
        else:
            print('\nНайденные контакты:\n')
            head = ['Имя', 'Фамилия', 'Отчество', 'Номер телефона']
            print(tabulate(data, headers=head, tablefmt="grid"))
            input("Нажмите Enter для продолжения...")
    file.close()