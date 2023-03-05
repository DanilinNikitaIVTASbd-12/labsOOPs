import csv
import os.path
import os

lst = os.listdir("D://3lab") # директория
number_files = len(lst)
print (number_files)
print("\n")

def print_date(dict): # вывод таблицы
    for a,b in dict.items():
        print(
            f"Id{a}: номер = {b['number']}, дата = {b['date']}, время = {b['time']}, сумма = {b['summ']}, описание = {b['opis']}")

def parse_csv(file):  # парсинг файла
     got_data = {}
     with open(file, "r", encoding='utf-8') as raw_csv:
         for line in raw_csv:
             (idx, number, date, time, summ, opis) = line.replace("\n", "").split(",")
             got_data.update({int(idx): {"number": int(number), "date": date, "time": time, "summ": summ, "opis": opis}})
     return got_data

def sort_by_data(c) -> dict:  # сортировка по первому числу в дате
    return dict(sorted(c.items(), key=lambda f: f[1]["date"]))

def sort_by_number(c) -> dict:  # сортировка по номеру
    return dict(sorted(c.items(), key=lambda f: f[1]["number"]))

def sort_by_values(c,value)->dict: # сортировка по номеру больше значения
    return dict((a, b) for a, b in c.items() if b["number"] > value)

data = parse_csv('D:\\3lab\\data.csv.txt') #путь до файла

print_date(data)#вывод таблицы
print("\n")

print_date(sort_by_data(data)) #сортировка по дате
print("\n")

print_date(sort_by_number(data)) #сортировка по номеру больше значения
print("\n")

print_date(sort_by_values(data, 13)) #сортировка по значению номера больше 13

def add(file,d,number,date,time,summ,opis): #функция сохранения
    with open(file, "w",encoding='utf-8') as f:
        for a,b in d.items():
            f.write(f"{a},{b['number']},{b['date']},{b['time']},{b['summ']}.{b['opis']}\n")
        f.write(f"{len(d) + 1},{number},{date},{time},{summ},{opis}\n")
    d.update({len(d) + 1: {"number": int(number), "date": date, "time": time, "summ": summ, "opis": opis}})
#add('D:\\3lab\\data.csv.txt', data, 555, '31.01.2023', "13:28", 200 , 'перевод') #добавление новых данных в файл

