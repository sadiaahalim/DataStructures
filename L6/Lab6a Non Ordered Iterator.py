

class TwoSet:
    def __init__(self):
        self.set1 = set()
        self.set2 = set()
        self.num_elts = 0
        self.data = []

    def put(self, x):
        if x not in self.set1:
            self.set1.add(x)
            return
        self.set2.add(x)
        

    def has(self, x):
        return x in self.set1 or x in self.set2

    def remove(self, x):
        if x in self.set1:
            self.set1.remove(x)
            return
        self.set2.remove(x)

    

    def count(self, x):
        total = 0
        if x in self.set1:
            total += 1
        if x in self.set2:
            total += 1
        return total

    def size(self):
        return len(self.set1) + len(self.set2)

    def distinct(self):
        temp = set()
        for x in self.set1:
            temp.add(x)
        for x in self.set2:
            temp.add(x)
        return len(temp)
    
    def debug(self):
        self.my_list()
        #print(self.data)
        #print(self.set1, self.set2)
        
    def my_list(self):
        for x in self.set1:
            self.data.append(x)
            self.num_elts += 1
        for x in self.set2:
            self.data.append(x)
            self.num_elts += 1
        return self.data
    
    def __iter__(self):
        self.pos = 0
        return self
    
    def __next__(self):
        if self.pos < self.num_elts:
            item = self.data[self.pos]
            self.pos += 1
            return item
        else:
            raise StopIteration



ts = TwoSet()
ts.put(12)
ts.put(45)
ts.put(13)
ts.put(13)
ts.put(13)
ts.put(48)
ts.debug()

l = []
for x in ts:
    print(x)


    

def union(ts1, ts2):
    result = TwoSet()
    for x in ts1.set1:
        result.put(x)
    for x in ts1.set2:
        result.put(x)
    for x in ts2.set1:
        result.put(x)
    for x in ts2.set2:
        result.put(x)

    return result


def intersect(ts1, ts2):
    result = TwoSet()
    for x in ts1.set1:
        if x in ts2.set1:
            result.put(x)
    for x in ts1.set2:
        if x in ts2.set2:
            result.put(x)

    return result


def difference(ts1, ts2):
    result = TwoSet()
    for x in ts1.set1:
        if x not in ts2.set1:
            result.put(x)
    for x in ts1.set2:
        if x not in ts2.set2:
            result.put(x)

    return result

