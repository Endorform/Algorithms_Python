
# coding: utf-8

# In[21]:


#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random


array = [0]*10
for i in range(len(array)):
    array[i] = random.randint(0, 100)
    print(array[i], end=' ')
print()

mn = 0
mx = 0
for i in range(len(array)):
    if array[i] < array[mn]:
        mn = i
    elif array[i] > array[mx]:
        mx = i
print(f"Минимальное значение - {array[mn]}, максимальное значение - {array[mx]}")
temp = array[mn]
array[mn] = array[mx]
array[mx] = temp
 
for i in range(len(array)):
    print(array[i], end=' ')
print()

