
# coding: utf-8

# In[24]:


#Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
#Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
#в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.

from statistics import median

import random 

m = int(input("Введите натуральное число m: "))

a = [0]*((2*m)+1)

#Заполняем случайным образом массив
for i in range(len(a)):
    a[i] = random.randint(-100, 100)

#Алгоритм сортировки, который используется в функции нахождения медианы
def select_nth(n, items):
    pivot = random.choice(items)

    lesser = [item for item in items if item < pivot]
    if len(lesser) > n:
        return select_nth(n, lesser)
    n -= len(lesser)

    numequal = items.count(pivot)
    if numequal > n:
        return pivot
    n -= numequal

    greater = [item for item in items if item > pivot]
    return select_nth(n, greater)

#Функция поиска медианы
def my_median(items):
    if len(items) % 2:
        return select_nth(len(items)//2, items)

    else:
        left  = select_nth((len(items)-1) // 2, items)
        right = select_nth((len(items)+1) // 2, items)

        return (left + right) / 2


print(f"Исходный список:\n{a}")
print(f"Медиана:\n{my_median(a)}")
print(f"Statistics.median:\n{median(a)}") # :-D - вариант без алгоритма сортировки

