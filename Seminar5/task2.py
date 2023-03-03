# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def ReplaceScore(lis):
    # print(min(lis))
    maximum = max(lis)
    minimum = min(lis)
    result = lis
    for i in range(len(result)):
        if result[i] == maximum: result[i] = minimum
    return result

# col = int(input('Сколько оценок хотите ввести? '))
score = [int(i) for i in input('Введите оценки через пробел: ').split()]
result = ReplaceScore(score)
print(result)