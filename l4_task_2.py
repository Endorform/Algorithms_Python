
# coding: utf-8

# In[38]:


#Написать два алгоритма нахождения i-го по счёту простого числа. 
#Первый - использовать алгоритм решето Эратосфена. 
#Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

import cProfile
import itertools

#1. Без решета Эратосфена
def find_prime_i(iPrime):
    startNumber = 1
    primeList = []
    while True:
        if startNumber > 1:
            for i in range(2,startNumber):
                if (startNumber % i) == 0:
                    break
            else:
                primeList.append(startNumber)
        if (len(primeList) == iPrime):
            return primeList[-1]
            break
        else:
            startNumber += 1 
            continue
            
#find_prime_i(100)

#%timeit 
#1. 1.67 ms ± 151 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each) find_prime_i(100)
#2. 3.97 ms ± 423 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) find_prime_i(150)
#3. 7.25 ms ± 282 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) find_prime_i(200)

#cProfile
#1. 645 function calls in 0.002 seconds cProfile.run("find_prime_i(100)") 
#   1    0.002    0.002    0.002    0.002 <ipython-input-11-b7526af62145>:8(find_prime_i) 
#2. 1017 function calls in 0.004 seconds cProfile.run("find_prime_i(150)")
#   1    0.004    0.004    0.004    0.004 <ipython-input-12-674744d109a4>:8(find_prime_i)
#3. 1427 function calls in 0.008 seconds cProfile.run("find_prime_i(200)")
#   1    0.007    0.007    0.007    0.007 <ipython-input-13-97442148c0c0>:8(find_prime_i)


#2. С использованием решета

def erato_primes():
    D = {}
    yield 2
    for q in itertools.count(3, 2):
        p = D.pop(q, None)
        if p is None:
            yield q
            D[q*q] = q
        else:
            x = p + q
            while x in D or x % 2 == 0:
                x += p
            D[x] = p
            
def find_prime_i_erato(n):
    if n < 1:
        raise ValueError("n должно быть >= 1")
    for i, p in enumerate(erato_primes(), 1):
        if i == n:
            return p

#find_prime_i_erato(100000)

cProfile.run("find_prime_i_erato(100000)")
#%timeit 
#1. 142 µs ± 8.37 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each) find_prime_i_erato(100) 
#2. 248 µs ± 50.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each) find_prime_i_erato(150) 
#3. 299 µs ± 6.41 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each) find_prime_i_erato(200)

#cProfile
#1. 375 function calls in 0.000 seconds cProfile.run("find_prime_i_erato(100)")
#   1    0.000    0.000    0.000    0.000 <ipython-input-30-311d26608eb7>:58(find_prime_i_erato)
#2. 586 function calls in 0.000 seconds cProfile.run("find_prime_i_erato(150)")
#   1    0.000    0.000    0.000    0.000 <ipython-input-31-703798801fb9>:58(find_prime_i_erato)
#3. 749859 function calls in 0.605 seconds cProfile.run("find_prime_i_erato(100000)")
#   1    0.021    0.021    0.605    0.605 <ipython-input-38-1cd9e16fe87f>:58(find_prime_i_erato)

#Вывод:
#find_prime_i_erato существенно быстрее 

