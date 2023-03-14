from modulуsForManu import *

def Manu():
    flag = True
    while flag:
        print('\n1 --> Добавить контакт \n2 --> Вывести контакты \n3 --> Поиск по фамилии \n4 --> Выход')
        num = int(input('\nВыберите пункт меню: '))
        if num == 1: addData()
        if num == 2: printData()
        if num == 3: SearchData()
        if num == 4: flag = False