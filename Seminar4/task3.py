# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.


# n = int(input())
# # max_number = 1000 # Ошибка
# max_number = -1
# while n != 0:
#     # n = int(input()) # Ошибка
#     # if max_number > n: # Ошибка
#     if max_number < n:
#         max_number = n
#     n = int(input())
# print(max_number)

# n = int(input())
# max_number = -1
# # while n < 0: # Ошибка
# while n != 0:
#     # n = int(input()) # Ошибка
#     if max_number < n:
#         # n = max_number # Ошибка
#         max_number = n
#     n = int(input())
# # print(n) # Ошибка
# print(max_number)