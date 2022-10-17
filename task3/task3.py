#Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform

n =int(input('Введите размер списка: '))

lst = [round(uniform(0,11),2) for i in range(n)]
new_lst = [round(i%1,2) for i in lst]
print(lst, '**', max(new_lst) - min(new_lst))