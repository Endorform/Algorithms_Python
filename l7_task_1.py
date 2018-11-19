
# coding: utf-8

# In[5]:


# Никита Чупраков

# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, 
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы

import random

a = [0]*100

#Заполняем массив рандомными значениями
for i in range(len(a)):
    a[i] = random.randint(-100, 100)
print(f"Исходный массив:\n{a}")

#Функция сортировки по убыванию
def bubble_sort_reverse(array):
    for i in range(len(array)-1):
        for j in range((len(array)-1)-i):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
    
print(f"Отсортированный по убыванию массив:\n{bubble_sort_reverse(a)}")

