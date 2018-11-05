
# coding: utf-8

# In[48]:


#Определить, какое число в массиве встречается чаще всего.

import random

array = [0] * 15
for i in range(len(array)):
    array[i] = random.randint(0,10)
print(array)
 
num = array[0]
max_frq = 1 #счетчик максимальной частотности 
for i in range(len(array) - 1):
    frq = 1
    for k in range(i+1,len(array)):
        if array[i] == array[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]
if max_frq > 1:
    print(f"{max_frq} раз(а) встречается число {num}")
else:
    print("Нет повторяющихся элементов")
    

