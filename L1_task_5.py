
# coding: utf-8

# In[1]:


#Никита Чупраков

#Пользователь вводит две буквы. 
#Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

a = ord(input("Буква 1: "))
b = ord(input("Буква 2: "))
a = a - ord("a") + 1
b = b - ord("a") + 1
print(f"Позиции: {a} и {b}")
print("Между буквами символов: ", abs(a-b)-1)

