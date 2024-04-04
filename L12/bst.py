from astack import Stack
class BSTNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return "k: " +str(self.key) + ", v: " + str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.current = None

    def insert(self, k, v):
        if not self.root:
            self.root = BSTNode(k, v)
            return

        p = self.root
        while True:
            if k < p.key:
                if p.left:
                    p = p.left
                else:
                    p.left = BSTNode(k, v)
                    p.left.parent = p
                    return
            elif k > p.key:
                if p.right:
                    p = p.right
                else:
                    p.right = BSTNode(k, v)
                    p.right.parent = p
                    return
            else:
                p.value = v
                return

    def find(self, k):
        p = self.root
        while p:
            if p.key == k:
                return p.value
            if k < p.key:
                p = p.left
            else:
                p = p.right
        return None

    def remove(self, k):
        
        self.current = self.root

        while self.current is not None and self.current.key != k:
            self.parent = self.current
            if self.current.key < k:
                self.current= self.current.right
            else:
                self.current = self.current.left
        if self.current is None:
            print("K not found",k)
            return self.root
        
        if self.current.left is None or self.current.right is None:
            newCurr = None
            if self.current.left is None:
                newCurr = self.current.right
            else:
                newCurr = self.current.left
            if self.parent is None:
                return newCurr
            
            if self.current == self.parent.left:
                self.parent.left = newCurr
            else:
                self.parent.right = newCurr
            self.current = None
        
        else:
            p = None
            temp = None
            temp = self.current.right
            while(temp.left != None):
                p = temp
                temp = temp.left
                
            if p != None:
                p.left = temp.right
            else:
                self.current.right = temp.right

            self.current.key = temp.key
            temp = None

        return self.root
        

    def inorder_debug(self):
        s = Stack()
        self.current = self.root
        while True:
            
            while self.current is not None:
                s.push(self.current)
                self.current = self.current.left
            if self.current is None and not s.empty():
                self.current = s.pop()
                print(self.current)
                self.current = self.current.right
            


t = BinarySearchTree()
t.insert(44, "a")
t.insert(17, "b")
t.insert(88, "c")
t.insert(8, "d")
t.insert(32, "e")
t.insert(65, "f")
t.insert(97, "g")
t.insert(28, "h")
t.insert(54, "i")
t.insert(82, "j")
t.insert(93, "k")
t.insert(29, "l")
t.insert(76, "m")
t.insert(68, "n")
t.insert(80, "o")

t.remove(68)
t.inorder_debug()
