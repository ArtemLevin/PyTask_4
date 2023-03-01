# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random

len_list = [int(input("Enter the length of the list ")) for i in range(0, 2)]
list_ = [[int(input("enter the number as an element of the first collection ")) for i in range(1, len_list[j] + 1)] for
         j in range(0, 2)]
print(sorted([i for i in set(list_[0]) & set(list_[1])]))
