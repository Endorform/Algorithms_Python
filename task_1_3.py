
# coding: utf-8

# In[2]:


# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех 
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.

# P.S. Напишите в комментариях версию Python и разрядность ОС.

import sys

def show_memory(x, level=0):
    print("\t" * level, f"type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}")
    if hasattr(x, "__iter__"):
        if hasattr(x, "items"):
            for key, value in x.items():
                show_memory(key, level + 1)
                show_memory(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_memory(item, level + 1)   
                
# Lesson 1 Task 6
n = int(input("Введите номер буквы: "))
n = ord("a") + n - 1
print("Это буква", chr(n))

spam = [n]
show_memory(spam)

# Python 3.6.3 |Anaconda custom (64-bit)
# n = 25
# type = <class 'list'>, size = 72, object = [121] - spam
#	 type = <class 'int'>, size = 28, object = 121
# Итого занято переменными: 28

