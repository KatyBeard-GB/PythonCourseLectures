# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

def inputArray(size):
    array = []
    for i in range(size): array.append(int(input()))
    return array

# N = int(input('Введите размер 1 массива: '))
# arrayN = inputArray(N)
# M = int(input('Введите размер 1 массива: '))
# arrayM = inputArray(M)

# print([i for i in arrayN if i not in arrayM])