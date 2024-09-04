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

def stockspan(stocks):
    s = Stack()
    span = [1]
    s.push(1)
    for i in range(1, len(stocks)):
        counter = 1
        while s.size() > 0 and s.peek() < stocks[i]:
            counter += 1
            s.pop()
        if s.size() == 0:
            span.append(i + 1)
        else : 
            span.append(counter)
        s.push(stocks[i])
    return span

# other method is push index in stack 0 and mark ans as 1 intially start from 2 pop till get bigger or stack empty 
# if empty stack then index + 1 push in ans else ...found big so ans is index of current - index of big in stack


def stockspan2(stocks):
    s = Stack()
    span = [1]
    s.push(0)
    for i in range(1 , len(stocks)):
        while s.size() > 0 and stocks[s.peek()] < stocks[i]:
            s.pop()
        if s.size() == 0:
            span.append(i + 1)
        else : 
            span.append(i - s.peek())
        s.push(i)
    return span


if __name__ == "__main__":
    stocks = [1,2,3,4,1,2,1,1,3,6,1,1,3]
    print(stockspan2(stocks))
