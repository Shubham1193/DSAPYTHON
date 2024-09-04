class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else : 
            return "stack is empty"
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        return self.stack
    
def balancedBracket(equation):
    s = Stack()
    for i in equation:
        if (i == ")" or i == "}" or i == "]"):
            if i == ")":
                peekvalue = s.peek()
                if peekvalue == "(":
                    return True
                else :
                    while s.peek() != "(":
                        s.pop()
                    s.pop()
            if i == "]":
                peekvalue = s.peek()
                if peekvalue == "]":
                    return True
                else :
                    while s.peek() != "[":
                        s.pop()
                    s.pop()
            if i == "}":
                peekvalue = s.peek()
                if peekvalue == "{":
                    return True
                else :
                    while s.peek() != "{":
                        s.pop()
                    s.pop()
        else : 
            s.push(i)
    return False
                

if __name__ == "__main__":
   equation1 = "[(a+b) + (c+d)]"
   equation2 = "(a+b) + ((c+d))"

   # push everything to stack and check for close if close comes and check peek if immediate close find then means duplicate 
   # if not immediate open comes then pop till its open then pop that open also
   ans = balancedBracket(equation2)
   if ans == True : print("Duplicate")
   else : print("no duplicate")