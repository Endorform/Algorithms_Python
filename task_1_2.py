
# coding: utf-8

# In[1]:


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

#Lesson_1 Task_5
a = ord(input("Буква 1: "))
b = ord(input("Буква 2: "))
a = a - ord("a") + 1
b = b - ord("a") + 1
print(f"Позиции: {a} и {b}")
print("Между буквами символов: ", abs(a-b)-1)

spam = [a,b]
show_memory(spam)

# Python 3.6.3 |Anaconda custom (64-bit)
# a = f, b = f
#  type = <class 'list'>, size = 80, object = [6, 6] - spam
# 	 type = <class 'int'>, size = 28, object = 6
# 	 type = <class 'int'>, size = 28, object = 6
# Итого занято переменными: 56

