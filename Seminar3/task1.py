# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

#  Можно данное задание сделать с помощью set()

n = int(input('Сколько чисел вы хотите ввести? '))
numbers = list()
for i in range(n):
    numbers.append(int(input('Введите число списка: ')))
result = 0
k = 1
for i in numbers:
    if i not in numbers[k:]: result+=1
    k += 1
print(result)

# result = set(numbers)