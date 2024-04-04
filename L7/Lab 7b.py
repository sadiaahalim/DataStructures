class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.res = ""
        
    def __str__(self):
        return str(self.value)

class DigitChain:
    def __init__(self):
        self.start = None
        self.string = ""
        self.num_elts = 0
        
    def convert_int(self,x):
        return self.convert_str(str(x))

    def convert_str(self,x):
        for i in x:
            n = Node(int(i))
            n.next = self.start
            self.start = n
            self.num_elts +=1
               
    def __str__(self):
        string = ""
        ptr = self.start
        while ptr:
            self.string += str(ptr)
            ptr = ptr.next

        return self.string[::-1]


def add_digitchain(c1,c2):
    carry=0
    total = ""
    if c1.num_elts >c2.num_elts:
        big = c1
        small = c2
    else:
        big = c2
        small = c1
    start = big.start
    small_num_head = small.start
    while start is not None and small_num_head is not None:
        sum_val = start.value + small_num_head.value + carry
        if sum_val>=10:
            carry =1
            sum_val = sum_val%10
            total+=str(sum_val)
        else:
            total+=str(sum_val)
            carry=0
            
        start = start.next
        small_num_head = small_num_head.next
   
    while start is not None:
        if carry == 1:
            sum_val = start.value + carry
            total+= str(sum_val)
            start = start.next
        if sum_val>=10:
            carry =1
            sum_val = sum_val%10
            total+=str(sum_val)
        else:
            sum_val = start.value
            total+=str(sum_val)
            carry=0
        
        start = start.next
        result = DigitChain()
    total = total[::-1]
    result.convert_str(total)
    
    return result
            

c1 = DigitChain()
c1.convert_str("56788622")
print(c1)
c2= DigitChain()
c2.convert_int(354225)
print("+",c2)
print("--------")
print(add_digitchain(c1,c2))


