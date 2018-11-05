
# coding: utf-8

# In[32]:


#В массиве найти максимальный отрицательный элемент. 
#Вывести на экран его значение и позицию в массиве.

import random

array = []
for i in range(10):
        array.append(random.randint(-50, 50))
print(array)
 
i = 0
index = -1
while i < len(array):
        if array[i] < 0 and index == -1:
                index = i
        elif array[i] < 0 and array[i] > array[index]:
                index = i
        i += 1
 
print(f"Максимальный отрицательный элемент: {array[index]}. Позиция в массиве: {index}")

