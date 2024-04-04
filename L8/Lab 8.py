class Stack:
    def __init__(self):
        self.data = 10*[None]
        self.top = 0

    def push(self, x):
        if self.top >= len(self.data):
            raise Exception("Stack Overflow")
        self.data[self.top] = x
        self.top += 1

    def pop(self):
        if self.empty():
            raise Exception("Stack Underflow")
        v = self.data[self.top-1]
        self.top -= 1
        return v
        
    def top(self):
        return self.data[self.top-1]

    def empty(self):
        return self.top == 0
    
    def debug(self):
        print(self.data)

class Token:
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __str__(self):
        return str(self.value)

class BooleanEvaluator:
    def __init__(self):
        self.wordlist = ""
        self.priority = {'^':1, 'v':2}
        
    def load_rpn(self,expression):
        for t in expression:            
            if t.upper() == "T":
                self.wordlist+= "True "
                continue
            if t.upper() == "F":
                self.wordlist+= "False "
                continue
            if t == '^':
                self.wordlist+= "^ "
                continue
            if t == 'v':
                self.wordlist+= "v "
                continue
            
            
    def load_infix(self,expression):
        stack = []
        expression = expression.replace(" ", "")
        for o in expression:
            if o.upper() == "T":
                self.wordlist += "True "
                
            elif o.upper() == "F":
                self.wordlist += "False "
                
            elif o == "(":
                stack.append("(")
                
            elif o == ")":
                while stack and stack[-1] != '(':
                    self.wordlist += stack.pop() + " "
                stack.pop()
            else:
                while stack and stack[-1] != '(' and self.priority[stack[-1]] >= self.priority[o]:
                    self.wordlist += stack.pop()+ " "
                stack.append(o)
                
        while stack:
            self.wordlist += stack.pop()+ " "


    
    def evaluate(self):
        stack = Stack()
        for t in self.wordlist:            
            if t.upper() == "T":
                exp = Token(1,True)
                stack.push(exp)
                continue
            
            if t.upper() == "F":
                exp = Token(1,False)
                stack.push(exp)
                continue
            
            if t == '^':
                v1 = stack.pop()
                v2 = stack.pop()
                res = v1.value and v2.value
                exp = Token(1,res)
                stack.push(exp)
                continue
            
            if t == 'v':
                v1 = stack.pop()
                v2 = stack.pop()
                res = v1.value or v2.value
                exp = Token(1,res)
                stack.push(exp)
                continue
            
        final  = stack.pop()
        if not stack.empty():
            return "Error in expression"
        else:
            return final

    
    def display_rpn(self):
        print(self.wordlist)
                


b = BooleanEvaluator()
b.load_rpn("T T F ^ ^")
b.display_rpn()
print("Result:", b.evaluate())
print("=======")
b1 = BooleanEvaluator()
b1.load_infix("( T^ F )^(T v F)")
b1.display_rpn()
print("Result:", b1.evaluate())
print("=======")
b2 = BooleanEvaluator()
b2.load_infix("T v ( T ^ F ) v F ^(T v T)")
b2.display_rpn()
print("Result:", b2.evaluate())
print("=======")
b3 = BooleanEvaluator()
b3.load_infix("T ^ ( T v F )")
b3.display_rpn()
print("Result:", b3.evaluate())

