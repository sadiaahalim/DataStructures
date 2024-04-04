class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    
    def insert_front(self, x):
        n = Node(x)
        if self.head is None:
            self.head = n
            self.last = n
            return
        n.next = self.head
        self.head.prev = n
        self.head = n
        
    def insert_back(self, x):
        n = Node(x)
        n.next = None
        n.prev = self.last
        if self.head is None:
            self.head = n
            self.last = n
            return
        self.last.next = n
        self.last = n
    
    def debug_forward(self):
        self.last.next = None
        ptr = self.head
        while ptr is not None:
            print(ptr)
            ptr = ptr.next

    def debug_reverse(self):
        ptr = self.last
        
        while ptr is not None:
            print(ptr)
            ptr = ptr.prev

    def list_forward(self, x):
        data = []
        self.last.next = self.head
        ptr = self.head
        count = 0
        while count < x:
            data.append(ptr.value)
            ptr = ptr.next
            count +=1
        print(data)

    def delete_front(self):
        self.head = self.head.next

    def delete_back(self):
        self.last = self.last.prev


c = CircularLinkedList()
c.insert_front(12)
c.insert_front(71)
c.insert_front(55)
c.insert_back(35)
c.insert_back(56)
print("Forward")
c.debug_forward()
print("Reverse")
c.debug_reverse()
c.list_forward(12)
print("Remove First item") 
c.delete_front()
c.debug_forward()
print("Remove Last item") 
c.delete_back()
c.debug_reverse()
