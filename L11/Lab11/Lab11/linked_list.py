

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.itr_ptr = None

    def __str__(self):
        return str(self.value)


class LinkedListIterator:
    def __init__(self, ll):
        self.ptr = ll.start

    def current_value(self):
        return self.ptr.value

    def next(self):
        self.ptr = self.ptr.next

    def has_next(self):
        return self.ptr.next is not None

class LinkedList:
    def __init__(self):
        self.start = None
        self.last = None

    def insert_front(self, value):
        n = Node(value)
        if self.start is None:
            self.start = n
            self.last = n
            return
        n.next = self.start
        self.start.prev = n
        self.start = n

    def get_first(self):
        return self.start

    def get_last(self):
        return self.last

    def display_list(self):
        p = self.start
        while p:
            print(p)
            p = p.next

    def remove_front(self):
        value = self.start.value
        self.start = self.start.next
        return value

    def insert_back(self, value):
        node = Node(value)
        node.next = None
        if self.start is None:
            self.start = node
            self.last = node
            return

        self.last.next = node
        self.last = node

    def get_iterator(self):
        return LinkedListIterator(self)

