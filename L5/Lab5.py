import unittest

class TwoSet:
    def __init__(self):
        self.data = []
        

    #insert a new item into the TwoSet.  If there are already two
    #copies of the value x in the TwoSet, this operation will be ignored.
        
    def put(self,x): #Time Complexity: #O(n^2)
        while True: #O(n)
            if x not in self.data:
                self.data.append(x) #O(n)
                break
            if x in self.data and self.data.count(x) == 2: #O(n)
                break
            else:
                self.data.append(x) #O(n)
    
    #remove the element x from the TwoSet.  If there is no element with the
    #value of x in your TwoSet the ADT will ignore the operation.
                
    def remove(self,x): #Time Complexity: O(n)
        if x in self.data:
            self.data.remove(x)
        

    #return true or false depending on if the TwoSet contains
    #at least one copy of a value.
            
    def has(self,x): #Time Complexity: O(n)
        if x in self.data:
            return True
        else:
            return False

    #return the number of items in the TwoSet with the value x.
    #This function should return 0, 1, or 2.
        
    def count(self,x): #Time Complexity: O(n^2)
        if x in self.data:
            return self.data.count(x)
        else:
            return 0

        
    #return the total number of elements in the TwoSet, including
    #values that appear multiple times.
        
    def size(self): #Time Complexity: O(n)
        total = 0
        for i in self.data:
            total += 1
        return total
        
        
    #return the number of distinct values in the TwoSet.
    
    def distinct(self): #Time Complexity: O(n^3)
        total = []
        for i in self.data: #O(n)
            if i not in total: #O(n)
                total.append(i) #O(n)
        return len(total)

    #For debugging purposes
    def debug(self):   #Time Complexity: O(1)
        return self.data



ts1 = TwoSet()
ts2 = TwoSet()
ts1.put(3)
ts1.put(6)
ts1.put(3)
ts1.put(9)
ts1.put(5)
ts1.put(4)
ts1.put(1)
#ts1.remove(3)
ts1.remove(4)
print("Value available:",ts1.has(4))
print("Number of count:",ts1.count(0))
print("Length of Data",ts1.size())
print("Total Elements",ts1.distinct())
print("Ts1",ts1.debug())

ts2.put(1)
ts2.put(4)
ts2.put(5)
ts2.put(1)

ts2.put(2)
ts2.put(3)

ts2.remove(3)
#ts2.remove(3)
ts2.remove(4)
print("Value available:",ts2.has(4))
print("Number of count:",ts2.count(5))
print("Length of Data",ts2.size())
print("Total Elements",ts2.distinct())
print("Ts2",ts2.debug())


#Create a union between the TwoSet ts1 and the TwoSet ts2.
#Remember that you should never have more than 2 copies of each
#element after the operation.  The function should return a
#new TwoSet object.

def union(ts1,ts2): #Time Complexity: #O(n^3)
    ts1_union_ts2 = TwoSet()
    for i in ts1.data:  #O(n)
        ts1_union_ts2.put(i)  #O(n^2)
    for j in ts2.data:
        ts1_union_ts2.put(j)
    print("Union",ts1_union_ts2.debug())

union(ts1,ts2)


def intersect(ts1, ts2):   #Time Complexity: O(n^5)
    ts1_intersect_ts2 = TwoSet()
    for i in set(ts1.data): #O(n)
        a = ts1.data.count(i) #O(n)
        b = ts2.data.count(i) #O(n)
        if a < b:
            for j in range(a):#O(n)
                ts1_intersect_ts2.put(i)#O(n^2)
        if a == b:
            for j in range(a): #O(n)
                ts1_intersect_ts2.put(i) #O(n^2)
        if b < a:
            for j in range(b): #O(n)
                ts1_intersect_ts2.put(i)#O(n^2)
        

    print("Intersect:", ts1_intersect_ts2.debug())
   
intersect(ts1,ts2)

def difference(ts1,ts2): #Time Complexity: #O(n^4)
    ts1_diff_ts2 = TwoSet()
    for i in ts1.data: #O(n)
        if i not in ts2.data: #O(n)
            ts1_diff_ts2.put(i) #O(n^2)
    print("Difference",ts1_diff_ts2.debug())
    
difference(ts1,ts2)    

class TwoSetTest(unittest.TestCase):
    
    def test_basic_func_put(self):
        t1 = TwoSet()
        t1.put(11)
        t1.put(1)
        t1.put(41)
        print(t1.debug())
        
    def test_basic_func_count(self):
        t1 = TwoSet()
        t1.put(11)
        t1.put(1)
        t1.put(41)
        self.assertEqual(t1.count(1),1)
        
        
    def test_basic_func_has(self):
        t1 = TwoSet()
        t1.put(13)
        t1.put(21)
        t1.put(1)

        self.assertEqual(t1.has(1),True)
        
    def test_basic_func_remove(self):
        t1 = TwoSet()
        t1.put(1)
        t1.put(1)
        t1.put(4)
        t1.remove(4)

        self.assertEqual(t1.has(4),False)

    def test_basic_func_size(self):
        t1 = TwoSet()
        t2 = TwoSet()
        t1.put(76)
        t1.put(54)
        t2.put(34)
        t2.put(12)
        self.assertEqual(t1.size(),t2.size(),True)
        
    def test_basic_func_distinct(self):
        t1 = TwoSet()
        t1.put(81)
        t1.put(19)
        t1.put(16)

        self.assertEqual(t1.distinct(),3)
        
   
        
if __name__ == '__main__':
    unittest.main()

