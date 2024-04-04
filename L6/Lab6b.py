import operator,unittest

class ScoreBoard:
    def __init__(self): #Time Complexity: #O(1)
        self.data = []
        self.num_elts = 10
    
    def addScore(self,team, points, time): #Time Complexity: #O(n)
        for i in self.data: #O(n)
            if i['team'] == team:
                raise print('Team already exists')
        self.data.append({'team':team, 'points' :points,'time':time}) #O(n)
        self.place_in_order()


    def place_in_order(self):#Time Complexity: #O(n)
        self.data.sort(key=operator.itemgetter('team'))
        self.data.sort(key=operator.itemgetter('time'))
        self.data.sort(key=operator.itemgetter('points'), reverse = True)
        
    def clear(self): #Time Complexity: #O(1)
        self.data = []

    def debug(self):#Time Complexity: #O(n)
        for i in self.data[0:10]:
            print(i)
                

    def __iter__(self): #Time Complexity: #O(1)
        self.pos = 0
        return self
    
    def __next__(self): #Time Complexity: #O(1)
        if self.pos < self.num_elts:
            item = self.data[self.pos]
            self.pos += 1
            return item
        else:
            raise StopIteration
 

sb = ScoreBoard()

sb.addScore('Twilight Zone',200,15)
sb.addScore('Super Cool',190,20)
sb.addScore('GTH',185,9)
sb.addScore('East vs West',185,11)
sb.addScore('Seven Seas',130,18)
sb.addScore('Fluke Chaos',120,30)
sb.addScore('Limbo Skipper',115,45)
sb.addScore('Hammer Twist',100,21)
sb.addScore('Ghost',200,12)
sb.addScore('Blue Dragons',185,11)
sb.addScore('Ben Dragons',210,11)
sb.addScore('Ghost ka behen',200,13)

print("==Iter Operation==")
for x in sb:
    print(x)

print("+++++++++")
class ScoreBoardTest(unittest.TestCase):
    def test_basic_func_addScore(self):
        print("Test Cases")
        sb = ScoreBoard()
        sb.addScore('Elden Ring',200,17)
        sb.addScore('Call of Duty: Mobile',216,20)
        sb.addScore('Genshin Impact',185,15)
        sb.addScore('East vs West',185,15)
        sb.addScore('GRID Autosport',130,18)
        sb.addScore('Fluke Chaos',120,30)
        sb.addScore('Legends of Runeterra',132,45)
        sb.addScore('Hammer Twist',202,21)
        sb.addScore('Ghost',200,12)
        sb.addScore('Blue Dragons',189,11)
        sb.addScore('Ghost ka behen',100,12)
        sb.addScore('Seven Seas',140,13)
        sb.debug()
        
    def test_clear(self):

        sb = ScoreBoard()
        sb.addScore('Elden Ring',200,17)
        sb.addScore('Call of Duty: Mobile',216,20)
        sb.addScore('Genshin Impact',185,15)
        sb.addScore('East vs West',185,15)
        sb.addScore('GRID Autosport',130,18)
        sb.addScore('Fluke Chaos',120,30)
        sb.addScore('Legends of Runeterra',132,45)
        
        sb.clear()
        print("List after using clear :",sb.debug())

        
    def test_sortAlphabet(self):

        print("Alphabetical Order :")
        sb = ScoreBoard()
        sb.addScore('Genshin Impact',185,15)
        sb.addScore('East vs West',185,15)
        sb.addScore('Elden Ring',200,20)
        sb.addScore('Call of Duty: Mobile',200,20)
        sb.debug()
    
    def test_itemExists(self):

        sb = ScoreBoard()
        sb.addScore('Blue Dragons',189,11)
        sb.addScore('Blue Dragons',185,15)
        sb.addScore('GRID Autosport',130,18)
        sb.addScore('Fluke Chaos',120,30)
        sb.addScore('Legends of Runeterra',132,45)
        sb.debug()
        
    
if __name__ == '__main__':
    unittest.main()
    
