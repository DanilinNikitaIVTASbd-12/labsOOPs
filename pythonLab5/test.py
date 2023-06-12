class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
        while n is not None:
            print(n.item , " ")
            n = n.nref
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
                return
        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return
        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break;
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def mycount(self, x):
        c = 0
        n = self.start_node
        while n is not None:
            if n.item == x:
                c += 1
                n = n.nref
            else:
                n = n.nref
        return c

    def update(self):
        n = self.start_node
        while n is not None:
            eA = listA.mycount(n)
            # print(eA) A[8]: 3 3 4 5 2 3 5 9 B[7]: 1 2 3 4 5 2 5

            if eA >= 2:
                for j in listB:
                    if j == i:
                        eB = listB.mycount(j)
                        if eB >= 2:
                            listA.delete_element_by_value(i)
        return listA


list = DoublyLinkedList()
list.insert_at_end(1)
list.insert_at_end(1)
list.insert_at_end(2)
list.traverse_list()
print(list.mycount(1))

#list.traverse_list()
