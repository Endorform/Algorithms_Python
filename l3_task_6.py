
# coding: utf-8

# In[24]:


#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
#Сами минимальный и максимальный элементы в сумму не включать.

import random

array = [0]*15
for i in range(len(array)):
    array[i] = random.randint(-10, 10)
print(array)

min_id = 0
max_id = 0
for i in range(1, len(array)):
    if array[i] < array[min_id]:
        min_id = i 
    elif array[i] > array[max_id]:
        max_id = i
print(f"Минимальный элемент: {array[min_id]}\nМаксимальный элемент: {array[max_id]}")

if min_id > max_id:
    min_id, max_id = max_id, min_id

summ = 0
for i in range(min_id+1, max_id):
    summ += array[i]
print(f"Сумма элементов между минимальным и максимальным: {summ}")

