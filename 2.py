'''Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением 
дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''
def difference(array):

    array = list(filter(lambda x: x>0, map(lambda x: round(x-int(x),3), array)))
    return max(array) - min(array)

array = [1.1, 1.2, 3.1, 5, 10.01]
print(difference(array))