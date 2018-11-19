
# coding: utf-8

# In[26]:


# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
#заданный случайными числами на промежутке [0; 50). 
#Выведите на экран исходный и отсортированный массивы.

import random

a = [0] * 100

# Заполняем вещественный массив, отсекаем 2 знака после запятой 
for i in range(len(a)):
    a[i] = round(random.uniform(0, 50), 2)
print(f"Исходный массив:\n{a}")

#Функция сортировки методом слияния
def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1

merge_sort(a)

print(f"Отсортированный по возрастанию методом слияния массив:\n{a}")

