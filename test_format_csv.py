import os

os.chdir('D:\Learn/Python/buzzdata')

with open('buzzers.csv') as data:
    ignore = data.readline #игнорировать заголовок
    flights = {} #создать пустой словарь
    for line in data:
        k, v = line.split(',')
        flights[k] = v
        
print(data)