#!/usr/bin/env python
# coding: utf-8

# **Задача 1**. Дано слово из латинских букв. Напишите скрипт, который выводит на экран букву из середины слова (если число букв нечетное). Если букв четное число, то на экран выводятся две буквы из середины.  
# 
# Пример: для 'test' должно выводится 'es', для 'testing' - 't'

# In[1]:


def middle_char(txt):
   return txt[(len(txt)-1)//2:(len(txt)+2)//2]
txt = input("Your word: ")
print("Your middle character: ", middle_char(txt))


# **Задача 2**. Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек (их число может варьироваться):

# In[354]:


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки! "Познакомить" пары нам поможет функция zip, а в цикле распакуем zip-объект и выведем информацию в виде:
# 
# Идеальные пары:  
# Alex и Emma  
# Arthur и Kate  
# John и Kira  
# Peter и Liza  
# Richard и Trisha  

# **Внимание! Если количество людей в списках будет не совпадать, то мы никого знакомить не будет и выведем пользователю предупреждение, что кто-то может остаться без пары!**

# In[355]:


boys_list = ['Peter', 'Alex', 'John', 'Arthur', 'Jim']
girls_list = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys_list.sort()
girls_list.sort()
perfect_match = zip(boys_list, girls_list)
if len(boys_list) == len(girls_list):
    print('Идеальные пары:')
else:
    print('Предупреждение! Кто-то может остаться без пары! Но мы все же нашли идеальные пары для некоторых участников:')
for element in perfect_match:
    print(element[0], 'и', element[1])


# **Задача 3**. У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за недельный период по странам.
# Необходимо написать код, который рассчитает среднюю температуру за неделю в Цельсиях для каждой страны.

# In[1]:


countries_temperature = [
 ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
 ['Germany', [57.2, 55.4, 59, 59, 53.6, 55.4, 57.2]],
 ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
 ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4, 51.8]],
]


for countries in countries_temperature:
    for temperatures in countries[1]:
        sum_ = sum(countries[1])
        average = sum(countries[1]) / len(countries[1])
        average_rounded = round(average,2)
    
    print(f'Average weekly temperature in', countries[0], '=', average_rounded)
    
            


# **Задача 4.** Дан поток логов по количеству просмотренных страниц для каждого пользователя. Список отсортирован по ID пользователя. Вам необходимо написать алгоритм, который считает среднее значение просмотров на пользователя. 
# Т. е. надо посчитать отношение суммы всех просмотров к количеству уникальных пользователей.

# In[ ]:





# In[227]:


stream = [
    '2018-01-01,user1,3',
    '2018-01-07,user1,4',
    '2018-03-29,user1,1',
    '2018-04-04,user1,13',
    '2018-01-05,user2,7',
    '2018-06-14,user3,4',
    '2018-07-02,user3,10',
    '2018-03-21,user4,19',
    '2018-03-22,user4,4',
    '2018-04-22,user4,8',
    '2018-05-03,user4,9',
    '2018-05-11,user4,11',
]


# In[353]:


u1 = 'user1'
u2 = 'user2'
u3 = 'user3'
u4 = 'user4'

u1_views = 0
u2_views = 0
u3_views = 0
u4_views = 0

count_u1 = 0
count_u2 = 0
count_u3 = 0
count_u4 = 0


for log in stream:
    new_stream = log.split(',')        
    if new_stream[1] == u1:
        u1_views += (int(new_stream[2]))
        count_u1 += 1
    elif new_stream[1] == u2:
        u2_views += (int(new_stream[2]))
        count_u2 += 1
    elif new_stream[1] == u3:
        u3_views += (int(new_stream[2]))
        count_u3 += 1
    elif new_stream[1] == u4:
        u4_views += (int(new_stream[2]))
        count_u4 += 1
        
sess_1 = count_u1
sess_2 = count_u2 
sess_3 = count_u3 
sess_4 = count_u4

av_u1 = u1_views / count_u1
av_u2 = u2_views / count_u2
av_u3 = u3_views / count_u3
av_u4 = u4_views / count_u4
    
print(f'Cреднее значение просмотров user1: {av_u1}')
print(f'Cреднее значение просмотров user2: {av_u2}')
print(f'Cреднее значение просмотров user3: {av_u3}')
print(f'Cреднее значение просмотров user4: {av_u4}')

   


# **Задача 5**. Дана статистика рекламных кампаний по дням. Напишите алгоритм, который по паре дата-кампания ищет значение численного столбца. 
# Т. е. для даты '2018-01-01' и 'google' нужно получить число 25. 
# Считайте, что все комбинации дата-кампания уникальны.

# In[54]:


stats = [
    ['2018-01-01', 'google', 25],
    ['2018-01-01', 'yandex', 65],
    ['2018-01-01', 'market', 89],
    ['2018-01-02', 'google', 574],
    ['2018-01-02', 'yandex', 249],
    ['2018-01-02', 'market', 994],
    ['2018-01-03', 'google', 1843],
    ['2018-01-03', 'yandex', 1327],
    ['2018-01-03', 'market', 1764],
]


# In[71]:


input1 = ['2018-01-03', 'yandex']

found = 'false'

for rows in stats:
    if rows[0] == input1[0] and rows[1] == input1[1]:
        print(rows[2])
        found = 'true'
        break
if found == 'false':
    print("not found")



# **Задача 6**. Дан список вида:

# In[56]:


data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35]
]


# In[72]:





# Напишите код, который будет вычислять сумму элементов на диагонали. Т. е. 13+32+23+35.  
# Список может быть любой длины, но всегда является "квадратным" (количество элементов во вложенных списках равно их количеству).

# In[91]:


n = len(data)
sum_diagonal = 0
for x in range(n):
    sum_diagonal += data[x][x]

sum_diagonal

    


# In[ ]:





# In[ ]:




