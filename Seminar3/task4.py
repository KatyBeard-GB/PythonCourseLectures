# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

n = int(input('Сколько чисел вы хотите ввести? '))
array = list()
for i in range(n):
    array.append(int(input('Введите число списка: ')))
result = 0
for i in range(len(array)-1):
    if array[i] < array[i+1]: result += 1
print(result)