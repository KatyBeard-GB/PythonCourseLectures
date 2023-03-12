# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

from task1 import inputArray

def ColMinElement(array):
    result = 0
    for i in range(1,len(array)-1):
        if array[i-1] < array[i] > array[i+1]: result += 1
    return result

N = int(input('Введите размер массива: '))
arrayN = inputArray(N)
print(f'Количество элементов: {ColMinElement(arrayN)}')

