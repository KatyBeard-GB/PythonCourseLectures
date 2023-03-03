# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def SearchFib(a):
    if a in [2,3]: return 1
    return SearchFib(a-1) + SearchFib(a-2)

n = int(input('Введите номер числа Фибоначчи: '))
print(f'{n} число Фибоначчи равно {SearchFib(n)}')