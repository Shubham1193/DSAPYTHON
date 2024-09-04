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
    
def nextGreater(que):
    s = Stack()
    n = len(que) - 1
    ans = [-1]
    s.push(7)
    for i in range(n-1 , -1 , -1):
        while s.size() > 0 and s.peek() < que[i]:
            s.pop()
        if s.size() == 0:
            ans.append(-1)
        else : 
            ans.append(s.peek())
        s.push(que[i])
    return ans

def nextGreater2(que):   # cannot put value in stack because some value are not remove so we need thei pos to pop later and put to ans
    s = Stack()
    n = len(que)             # here to maintin which item are not poped we used index other wise no option to find the and place the element where it is not poped
    ans = [-1] * n 
    s.push(0)
    for i in range(1 , n):
        while s.size() > 0 and que[s.peek()] < que[i]:   # 0 < 5
            ans[s.peek()] = que[i] # ans[0] = 5
            s.pop() 
        s.push(i)
    # print(s.display())
    while s.size() > 0:
        ans[s.peek()] = -1
        s.pop()
    return ans

if __name__ == "__main__":
    que = [2,5,9,3,1,12,6,8,7]
    ans = nextGreater2(que)
    print(ans)
   