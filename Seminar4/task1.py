# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

string = input('Введите любую строку: ')
dict = {}
                                         #                            необязательно
for symbol in string:                    #                                  V  
    dict[symbol] = dict.get(symbol, 0)+1 # <словарь>.get(<ключ>,<значение по умолчанию>)
for key, value in dict.items():
    print(f'{key}_{value}')