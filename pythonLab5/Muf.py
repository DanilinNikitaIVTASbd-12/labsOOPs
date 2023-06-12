import random
class Node: #Класс для единственного узла в списке
    def __init__(self, data):
        self.item = data #Текущий элемент списка
        self.nref = None #Ссылка на следующий элемент
        self.pref = None #Ссылка на предыдущий элемент, т.к. узел единственный, то у него нет следующего и предыдущего элементов, их значения None

class DoublyLinkedList: #Класс содержащий функции списка
    def __init__(self):
        self.start_node = None

    def Myappend(self, data):#Добавление элемента в конец списка
        if self.start_node is None:#Проверяем список на пустоту
            new_node = Node(data) #Значение первого узла
            self.start_node = new_node #Добавляем элемент в пустой список
            return
        n = self.start_node #Присваиваем n значение первого узла
        while n.nref is not None: #Запускаем цикл до момента пока ссылка на след. эдемент не будет равна None
            n = n.nref #Следующий узел становится текущим
        new_node = Node(data) #Задаем значение
        n.nref = new_node #Присваиваем значения след. узлу
        new_node.pref = n #Текущий узел становится предыдущим

    def traverse_list(self): #Обход списка
        if self.start_node is None: # ПРоверка на пустоту
            print("В списке нет элементов")
            return
        else: #Если список не пустой то проходимся циклом и выводим каждый элемент
            n = self.start_node
        while n is not None:
            print(n.item , " ")
            n = n.nref
    def Myremove(self, x): #Удаление элемента по значению
        if self.start_node is None: #Проверка на пустоту
            print("В списке нет элемента для удаления")
            return
        if self.start_node.nref is None: #Проверка на наличие след. элемента
            if self.start_node.item == x: #Проверяем, тот ли это элемент, который нудо удалить
                self.start_node = None #Если да, то удаляем
            else:
                print("Элемент для удаления не найден")
                return
        if self.start_node.item == x: #Поверяем значение текущего узла
            self.start_node = self.start_node.nref #Присваиваем текущему узлу ссылку на след. элемент
            self.start_node.pref = None #Прыдущий элемент удаляем
            return
        n = self.start_node
        while n.nref is not None: #если список содержит несколько элементов и удаляемый элемент не является первым элементом, мы просматриваем все элементы в списке
            if n.item == x:#Проверяем, имеет ли какой-либо из узлов значение, соответствующее значению, которое нужно удалить
                break;
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref #Установливаем значение следующей ссылки предыдущего узла на следующую ссылку удаляемого узла
            n.nref.pref = n.pref #Установливаем предыдущее значение следующего узла на предыдущую ссылку удаляемого узла
        else: #если удаляемый узел является последним узлом
            if n.item == x:
                n.pref.nref = None #для следующей ссылки узла, предшествующего последнему узлу, устанавливается значение «None»
            else:
                print("Элемент для удаления не найден")

    def mycount(self, x):#Возвращает количество вхождений элемента в список
        c = 0 #Объявляем счетчик
        n = self.start_node
        while n is not None: #Проходимся по списку
            if n.item == x: #Если значение элемента списка совпадает с нежным нам значением x
                c += 1 # То пребавляем счетчик на единицу
                n = n.nref #И присваиваес текущиму узлу ссылку на следующий
            else:
                n = n.nref # Иначе присваиваес текущиму узлу ссылку на следующий
        return c #Возвращаем количество вхождений

    def update(self):#Основная логика
        n = self.start_node
        while n is not None: # Проходимся по списку A
            eA = listA.mycount(n.item) #Присваиваем в переменную eA количество вхождений текущего элемента
            if eA >= 2: #Проверяем, чтобы кол. вхождений было больше, либо равно 2
                n1 = listB.start_node
                while n1 is not None:# Проходимся по списку B
                    if n1.item == n.item: #Если значение элемента списка B равно значению элемента списка A
                        eB = listB.mycount(n1.item) #Присваиваем в переменную eB количество вхождений текущего элемента
                        if eB >= 2:#Проверяем, чтобы кол. вхождений было больше, либо равно 2
                            listA.Myremove(n.item) #Удаляем элемент с этим значением из списка A
                    n1 = n1.nref #присваиваес текущиму узлу ссылку на следующий в списке B
            n = n.nref#присваиваес текущиму узлу ссылку на следующий в списке A
        return listA #Возвращаем измененный список A

a = 0
listA = DoublyLinkedList() # создадим объект класса DoublyLinkedList
listB = DoublyLinkedList()# создадим объект класса DoublyLinkedList
"""
list.insert_at_end(1)
list.traverse_list()
list.delete_element_by_value(1)
list.traverse_list()
"""




def userInput(): #Функция ввода пользователя
    while True:
        try:
            a = int(input("Пожалуйста выберите, каким образом вы хотели бы заполнить список: вручную (введите 0) или автоматически случайными "
        "числами (введите 1): "))
        except ValueError:
            print("Пожалуйста введите целое число из предложенных вариантов")
        else:
            if ((a != 0) and (a != 1)): #обработка ошибки ввода
                print("Пожалуйста введите целое число из предложенных вариантов")
            else:
                return a
                break



a = userInput()

if a == 0: #Если спик заполняется вручную
    while True:
        try:
            nA = int(input("Пожалуйста введите количество элементов списка A: "))
            nB = int(input("Пожалуйста введите количество элементов списка B: "))
        except ValueError:
            print("Пожалуйста введите целое положительное число")
        else:
            if (nA <= 0):
                print("Пожалуйста введите целое положительное число")

            else:
                print("Пожалуйста введите элементы списка A: ")

                for i in range(nA):
                    while True:
                        try:
                            e = int(input())
                        except ValueError:
                            print("Пожалуйста введите целое число")
                        else:
                            listA.Myappend(e) # добавление элементов в список
                            break
                if (nB <= 0):
                    print("Пожалуйста введите целое положительное число")

                else:
                    print("Пожалуйста введите элементы списка B: ")

                    for i in range(nB):
                        while True:
                            try:
                                e = int(input())
                            except ValueError:
                                print("Пожалуйста введите целое число")
                            else:
                                listB.Myappend(e) # добавление элементов в список
                                break

                print("Список A до преобразования:")
                listA.traverse_list() #Вывод списка
                print("Список B до преобразования:")
                listB.traverse_list()
                listA.update()
                print("Список A после преобразования:")
                listA.traverse_list()
                break


else: #Если спик заполняется атоматически
    while True:
        try:
            nA = int(input("Пожалуйста введите количество элементов списка A: "))
            nB = int(input("Пожалуйста введите количество элементов списка B: "))
        except ValueError:
            print("Пожалуйста введите целое положительное число")
        else:
            if (nA <= 0):
                print("Пожалуйста введите целое положительное число")
            else:
                while True:
                    try:
                        lA = int(input("Пожалуйста введите значение левой границы диапазона для генерации случайных чисел списка A: "))
                        rA = int(input("Пожалуйста введите значение правой границы диапазона для генерации случайных чисел списка A: "))
                    except ValueError:
                        print("Пожалуйста введите целое число")
                    else:
                        for i in range(nA):
                            e = random.randint(lA, rA) #Используется рандомайзер, для заполнения, в пределах от lA до rA

                            listA.Myappend(e)
                        break
                if (nB <= 0):
                    print("Пожалуйста введите целое положительное число")
                else:
                    while True:
                        try:
                            lB = int(input(
                                "Пожалуйста введите значение левой границы диапазона для генерации случайных чисел списка B: "))
                            rB = int(input(
                                "Пожалуйста введите значение правой границы диапазона для генерации случайных чисел списка B: "))
                        except ValueError:
                            print("Пожалуйста введите целое число")
                        else:
                            for i in range(nB):
                                e = random.randint(lB, rB)

                                listB.Myappend(e)
                            break

                print("Список A до преобразования:")
                listA.traverse_list()
                print("Список B до преобразования:")
                listB.traverse_list()
                listA.update()
                print("Список A после преобразования:")
                listA.traverse_list()
        break






