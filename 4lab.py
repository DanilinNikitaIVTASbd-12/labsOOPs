import csv  # Библиотека импорта и экспорта для электронных таблиц и баз данных
import datetime


# Родительский класс "Человек"
class Person:
    # Метод инициализации экземпляров класса после их создания
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age(age)
        self.__gender = gender

    def __age(self, value):
        if value <= 120:
            self.__age = value

    # Статические метод проверки на совершеннолетие
    @staticmethod
    def is_adult(age):
        return age >= 18

    # Метод (сеттер) для получения имени человека
    def setName(self, newName):
        self.__name = newName

    # Метод (сеттер) для получения возраста человека
    def setAge(self, newAge):
        if newAge <= 120:
            self.__age = newAge

    # Метод (сеттер) для получения пола человека
    def setGender(self, newGender):
        if (newGender == "Male") or (newGender == "Female"):
            self.__gender = newGender

    # Метод (геттер) для изменения имени человека
    def getName(self):
        return self.__name

    # Метод (геттер) для изменения возраста человека
    def getAge(self):
        return self.__age

    # Метод (геттер) для изменения пола человека
    def getGender(self):
        return self.__gender


# Дочерний класс "Пользователь", наследованный от родительского класса "Человек"
class User(Person):
    def __init__(self, name, age, gender, n, date, time, sum, assessment_description):
        Person.__init__(self, name, age, gender)
        self.__n = n
        self.__dates = []
        self.login(date)
        self.__time = time
        self.__sum = sum
        self.__assessment_description = assessment_description

    # Метод, который вызывается при соверщении операции
    def login(self, date):
        self.__dates.append(date)

    # Кастомный итератор класса (описание ниже)
    def __iter__(self):
        return UserDateIterator(self.__dates)

    # Переопределённый метод вывода информации об объекте класса "Пользователь"
    def __repr__(self):
        # Если сегодня пользователь совершал операцию

        if (datetime.datetime.now().strftime("%d.%m.%Y") == self.__dates[len(self.__dates) - 1]):
            # Значит он онлайн (время не учитывается)
            return f"{self.__n}. Name = {self.getName()}, age = {self.getAge()}, Time = {self.__time}, Sum = {self.__sum}"
        else:
            # Иначе он оффлайн (выводим, когда пользователь совершал операцию последний раз)
            return f"{self.__n}. Name = {self.getName()}, age = {self.getAge()} Sum = {self.__sum}, Date =  {self.__dates[len(self.__dates) - 1]}, {self.__time})"

    # Генератор для перебора списка дат совершения операций
    def generator(self, i):
        while i < len(self.__dates):
            yield self.__dates[i]  # Ключевое слово yield возвращает нас обратно в этот метод, запоминая состояние выхода
            i += 1
        else:
            yield 0

    # Метод присвоения значения value какому-либо атрибуту key объекта класса "Пользователь"
    def __setattr__(self, key, value):
        self.__dict__[key] = value

    # Метод позволяет получить значение какого-либо атрибута объекта класса "Пользователь" по его индексу
    def __getitem__(self, item):
        s = "_User__" + item
        return self.__dict__[s]


# Класс кастомного итератора для класса "Пользователь"
class UserDateIterator():
    # При создании итератора, получаем список дат выполненныйх опреаций и инициализируем счётчик для его обхода
    def __init__(self, dates):
        self.dates = dates
        self.i = 0

    # Метод возвращает следующий элемент из списка посещений
    def __next__(self):
        if self.i < len(self.dates):
            date = self.dates[self.i]
            self.i += 1
            return date
        else:
            return 0


fI = open("C:\\Users\\Molniya\\Desktop\\data.csv", 'r')  # Открываем файл для чтения (read)
# Класс DictReader модуля csv создаёт объект, который работает как обычный reader(), но отображает информацию о каждой строке в качестве словаря dict
reader = csv.DictReader(fI, fieldnames = None, restkey = None, restval = None, dialect = "excel")

l = []

for row in reader:
    # Создаём объект класса пользователя и добавляем его в список
    a = User(row["Name"], int(row["Age"]), row["Gender"], int(row['N']), row["Date"], row["Time"], int(row["Sum"]), row["Assessment_description"])
    l.append(a)

print("Исходные данные: ")
print(l)

l[2].setAge(17)

l[2].login("17.02.2023")

print(l)
print()

# Сортируем список при помощи лямбда-функции по столбцу с именем из таблицы
sSL = sorted(l, key = lambda d: d.getName())
# Сортируем список при помощи лямбда-функции по столбцу с номером клиента из таблицы и переворачиваем список (reverse)
nSL = sorted(l, key = lambda d: d['n'], reverse = True)

print("Сортировка по строковому полю (имени): ")
print(sSL)
print("Сортировка по числовому полю (номеру посетителя) в обратном порядке (reverse): ")
print(nSL)

newL = []

# Отбор пользователей по совершеннолетию (только те, кому больше 17 лет)
newL = list(filter(lambda x: x.is_adult(x.getAge()), l))
print("Совершеннолетние пользователи: ")
print(newL)

# Создаём файл для записи
with open("C:\\Users\\Molniya\\Desktop\\data.csv", 'w', newline = '') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = reader.fieldnames)  # Класс writer служит для записи данных в файл
    writer.writeheader()  # Записываем заголовок таблицы

    for row in sSL:
        d = {}
        d['N'] = row['n']  # Доступ к элементам коллекции по индексу осуществляется при помощи метода __getitem__
        d['Date'] = row['dates'][-1]
        d['Time'] = row['time']
        d['Sum'] = row['sum']
        d['Assessment_description'] = row['assessment_description']
        d['Gender'] = row.getGender()
        d['Age'] = row.getAge()
        d['Name'] = row.getName()

        # Метод writerow записывает словарь со значениями в файл
        writer.writerow(d)

    for row in nSL:
        d = {}
        d['N'] = row['n']

        # Запись даты через итератор класса
        iterator = iter(row)
        b = next(iterator)
        d['Date'] = str(b)

        while (b):
            b = next(iterator)

            if (b != 0):
                d['Date'] = str(b)
        #

        d['Time'] = row['time']
        d['Sum'] = row['sum']
        d['Assessment_description'] = row['assessment_description']
        d['Gender'] = row.getGender()
        d['Age'] = row.getAge()
        d['Name'] = row.getName()

        writer.writerow(d)

    for row in newL:
        d = {}
        d['N'] = row['n']

        # Запись даты через генератор класса
        i = 0

        generator = row.generator(i)
        b = next(generator)
        d['Date'] = str(b)

        while (b):
            b = next(generator)

            if (b != 0):
                d['Date'] = str(b)
        #

        d['Time'] = row['time']
        d['Sum'] = row['sum']
        d['Assessment_description'] = row['assessment_description']
        d['Gender'] = row.getGender()
        d['Age'] = row.getAge()
        d['Name'] = row.getName()

        writer.writerow(d)

print()
print("Пожалуйста, проверьте выходной файл")

