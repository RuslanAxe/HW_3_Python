# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
# Последняя строка содержит число X.
# *Пример:*
# 5
#     7 -2 3 5 1
#     3
#     -> 1
import random
n = int(input("Введите размер списка "))
lst = [random.randint(-9, 9) for i in range(n)]
print(lst)
x = int(input("Введите число для поиска: "))
count = 0
for i in lst:
    if i == x:
        count += 1 
# print(lst.count(x))
print(count)
