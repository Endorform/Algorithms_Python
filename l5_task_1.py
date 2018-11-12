
# coding: utf-8

# In[35]:


#Никита Чупраков

#Пользователь вводит данные о количестве предприятий, 
#их наименования и прибыль за 4 квартала для каждого предприятия. 
#Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, 
#чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import deque

total_comp_ledger = {} #Здесь будут все данные от всех компаний
loser_comps = [] #Список компаний, прибыль которых ниже средней
winner_comps = [] #Список компаний, прибыль которых выше средней
comp_av_profit = [] #Значение средней прибыль всех компаний (за год)

comp_num = int(input("Введите количество предприятий: "))

for i in range(comp_num):
    comp_name = input(f"\nВведите наименование предприятия №{i+1}: ")
    comp_profit_1 = int(input(f"\nВведите прибыль компании {comp_name} за 1-й квартал: "))
    comp_profit_2 = int(input(f"\nВведите прибыль компании {comp_name} за 2-й квартал: "))
    comp_profit_3 = int(input(f"\nВведите прибыль компании {comp_name} за 3-й квартал: "))
    comp_profit_4 = int(input(f"\nВведите прибыль компании {comp_name} за 4-й квартал: "))
    av_profit = (comp_profit_1 + comp_profit_2 + comp_profit_3 + comp_profit_4)/4 #Высчитываем общую прибыль за год
    comp_ledger = {"Имя компании": comp_name, "Прибыль 1-й квартал": comp_profit_1, "Прибыль 2-й квартал": comp_profit_2, 
                   "Прибыль 3-й квартал": comp_profit_3, "Прибыль 4-й квартал": comp_profit_4, 
                   "Средняя прибыль": av_profit}
    total_comp_ledger[f"Компания №{i+1}"] = comp_ledger #Добавляем данные о компании в общий словарь

comp_av_profit = deque([])
for i in range(comp_num):
    #Записываем в список значения средней прибыли
    comp_av_profit.append(total_comp_ledger[f"Компания №{i+1}"]["Средняя прибыль"])  

spam = 0 #Переменная для подсчета средней прибыли для всех компаний 

for i in comp_av_profit:
    spam = spam + i

total_comp_av_profit = spam/comp_num #Средняя годовая прибыль для всех компаний

#Разносим компании по спискам в зависимости от годовой прибыльности 
for i in range(comp_num):
    if total_comp_ledger[f"Компания №{i+1}"]["Средняя прибыль"] < total_comp_av_profit:
        loser_comps.append(total_comp_ledger[f"Компания №{i+1}"]["Имя компании"])
    else:
        winner_comps.append(total_comp_ledger[f"Компания №{i+1}"]["Имя компании"])

print(f"\nСредняя прибыль для всех компаний за год: {total_comp_av_profit}")
print(f"\nКомпании, чья прибыль ниже средней годовой прибыли: {loser_comps}")
print(f"\nКомпании, чья прибыль выше средней годовой прибыли: {winner_comps}")

# Если нужно будет распечатать всю базу:
# for key, value in total_comp_ledger.items():
#     print("*"*70)
#     print(f"{key}:")
#     for key_1, value_1 in value.items():
#         print(f"\n{key_1}:{value_1}")

