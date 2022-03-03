import os
from pprint import pprint
from datetime import datetime

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

os.chdir('D:\Learn/Python/buzzdata')

with open('buzzers.csv') as data:
    ignore = data.readline #игнорировать заголовок
    flights = {} #создать пустой словарь
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
        
#pprint(flights)


flights2 = {}

for k, v in flights.items(): #метод items возвращает элекменты словаря по одному
    flights2[convert2ampm(k)] = v.title()
    
#pprint(flights2)

more_flights = {} #генератор словарей

more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}

#pprint(more_flights)

just_freeport2 = {convert2ampm(k): v.title() 
                  for k, v in flights.items() 
                  if v == 'FREEPORT'}

#pprint(just_freeport2)

data = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
evens = [num 
         for num in data 
         if not num % 2]

data = [ 1, 'one', 2, 'two', 3, 'three', 4, 'four' ]
words = [num for num in data if isinstance(num, str)]

data = list('So long and thanks for all the fish'.split())
title = [word.title() for word in data]

when = {}
for dest in set(flights.values()):
    when[dest] = [k for k, v in flights.items() if v == dest]

when2 = {dest: [k for k, v in flights.items() if v == dest] for dest in set(flights.values())}

pprint(when2)       
