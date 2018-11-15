
# coding: utf-8

# In[25]:


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

#Lesson_1 Task_1
num = int(input("Введите трехзначное число, чтобы посчитать сумму и произведение его цифр: "))
 
d1 = num % 10
d2 = num % 100 // 10
d3 = num // 100
 
print("Сумма цифр:", d1 + d2 + d3)
print("Произведение цифр:", d1 * d2 * d3)


print("*" * 100)
spam = [num, d1, d2, d3]
show_memory(spam)

# Python 3.6.3 |Anaconda custom (64-bit)
# Введено значение num = 25
#  type = <class 'list'>, size = 96, object = [25, 5, 2, 0] - temp список с переменными
# 	 type = <class 'int'>, size = 28, object = 25
# 	 type = <class 'int'>, size = 28, object = 5
# 	 type = <class 'int'>, size = 28, object = 2
# 	 type = <class 'int'>, size = 24, object = 0
# Итого занято переменными: 108 

