
# coding: utf-8

# In[38]:


#Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.


# Task_5 Lesson_3 В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

#Немного переработана - обернуто в функцию, print`ы заменены на return

import random
import cProfile

def my_func(array_length):
    array = []
    for i in range(array_length):
        array.append(random.randint(-50, 50))

    i = 0
    index = -1
    while i < len(array):
        if array[i] < 0 and index == -1:
            index = i
        elif array[i] < 0 and array[i] > array[index]:
            index = i
        i += 1

    return array[index], index

my_func(100)

#%timeit 
#1. 18.5 µs ± 2.82 µs per loop (mean ± std. dev. of 7 runs, 100000 loops each) my_func(10)
#2. 169 µs ± 14.3 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each) my_func(100)
#3. 1.51 ms ± 30.6 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each) my_func(1000)
#4. 14.9 ms ± 146 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) my_func(10000)

#1. cProfile.run("my_func(10000)") 72773 function calls in 0.026 seconds 
#       1    0.007    0.007    0.026    0.026 <ipython-input-24-ce33226ad59f>:13(my_func)
#2. cProfile.run("my_func(100000)") 726764 function calls in 0.296 seconds 
#       1    0.075    0.075    0.295    0.295 <ipython-input-26-6ee9bb19fb47>:13(my_func)
#3. cProfile.run("my_func(1000000)") 7267528 function calls in 2.712 seconds
#       1    0.710    0.710    2.701    2.701 <ipython-input-27-9f3d002e0231>:13(my_func)

