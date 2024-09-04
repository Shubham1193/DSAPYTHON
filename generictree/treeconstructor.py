class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

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
    

def display(node):
    printdata = node.data
    print(printdata , end = " -> ")
    for i in node.children:
        print(i.data , end=" ")
    print()
    for i in node.children:
        display(i)

def sizeoftree(node):    # count of nodes
    count = 1
   
    for i in node.children: # 1 + size of 20 , then 30 then 40
        cs = sizeoftree(i)
        count += cs

    return count

def heightoftree(node):
    height = -1         # why -1 beacause think of 10 only tree height in case of edges is 0 and if nodes kae term mae then initalize it wiht 0 
    for i in node.children:
        ch = heightoftree(i)      # heigth of 20 30 40 ka max then compaare then + -1
        if ch > height:
            height = ch
    height += 1
    return height

def maxoftree(node):
    max = 0
    for i in node.children:
        cmax = maxoftree(i)  # 20 30 40 max one by one and compare and save to
        if cmax > max:
            max = cmax
    if max < node.data:
        max = node.data
    return max

# build a tree u

if __name__ == "__main__":
    treedata = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100]

    s = Stack()
    root = None
    for i in treedata:
        if i == -1:
            s.pop()
        else :
            node = Node(i)
            if s.size() > 0:
                peek = s.peek()
                peek.children.append(node)
                s.push(node)
            else :
                root = node
                s.push(node)
    display(root)
    print(sizeoftree(root))
    print(maxoftree(root))