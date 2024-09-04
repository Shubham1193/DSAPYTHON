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

def checkBalanced(equation):

    s = Stack()
    for i in equation :
        if (i == "[" or i == "{" or i == "(") :
            s.push(i)
        elif (i == "]" or i == "}" or i == ")"):
            if s.size() > 0 :     # more closing 
                if i == ")":
                    peekvalue = s.peek()
                    if peekvalue == "(":
                        s.pop()
                    else : 
                        return False
                elif i == "}":
                    peekvalue = s.peek()
                    if peekvalue == "{":
                        s.pop()
                    else : 
                        return False
                elif i == "]":
                    peekvalue = s.peek()
                    if peekvalue == "[":
                        s.pop()
                    else : 
                        return False
            else : 
                return False
        
            
    if s.size() > 0 : return False   # more opening
    else : return True

if __name__ == "__main__":

    equation = "[(a+b) + {(c+d) * (c+d)}]"
    equation2 = "[(a+b) + (c+d) * (c+d)}]"
    ans = checkBalanced(equation2)
    

    if ans == True: print("balaced")
    else : print("unbalaced")

   
    