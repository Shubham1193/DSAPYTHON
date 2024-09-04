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
    
def nseonleft(areas):
    s = Stack()
    ans = [0]
    s.push(0)
    for i in range(1 , len(areas)):
        counter = 0
        while s.size() > 0 and areas[s.peek()] > areas[i]:
            counter += 1
            s.pop()
        if s.size() == 0:
            ans.append(i)
        else :
            ans.append(counter)
        s.push(i)
    return ans

        
def nseonright(areas):
    s = Stack()
    ans = [0]
    s.push(len(areas) - 1)
    for i in range(len(areas) - 2 , -1 , -1):
        counter = 0
        while s.size() > 0 and areas[s.peek()] > areas[i]:
            counter += 1
            s.pop()
        ans.append(counter)
        s.push(i)
    return list(reversed(ans))


if __name__ == "__main__" :
    areas = [6,2,5,4,5,1,6]
    # i am able to see that find next smaller on right and left for curr and widh is diff of both and area is diff * hight of curr
    nsl = nseonleft(areas)
    nsr = nseonright(areas)
    print(nsl)
    print(nsr)
    for i in range(len(areas)):
        width = nsl[i] + nsr[i] + 1
        area = width * areas[i]
        print(area)
