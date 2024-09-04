class Node:
    def __init__(self , data):
        self.data = data
        self.children = []


class Queue:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            temp = list(reversed(self.stack))
            val = temp.pop()
            self.stack = list(reversed(temp))
            return val
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
    

def levelOrder(root):
    q = Queue()
    q.push(root)
    while q.size() > 0 :
        node = q.pop()
        print(node.data)
        for i in node.children:
            q.push(i)

def levelOrderlinewise(root):
    mq = Queue()
    cq = Queue()
    mq.push(root)
    while mq.size() > 0:
        node = mq.pop()
        print(node.data , end = " ")
        for i in node.children:
            cq.push(i)
        if mq.size() == 0:
            mq = cq
            cq = Queue()
            print()

def levelOrderlinewisedelimieter(root):
    q = Queue()
    q.push(root)
    q.push(Node(-1))
    while q.size() > 0 :
        node = q.pop()
        if node.data == -1:
            if q.size() > 0:  # Only push another delimiter if there are more nodes to process
                #eg 10 null 20 30 40 
                q.push(Node(-1))
            print()
        else :
            print(node.data , end= " ")
            for i in node.children:
                q.push(i)
        

def levelOrderlinewiseCount(root):
    q = Queue()
    q.push(root)
    while q.size() > 0 :
        count = q.size()
        for i in range(0 , count):
            node = q.pop()
            print(node.data , end= " ")
            for i in node.children:
                q.push(i)
        print()

# pair class 
class Pair:
    def __init__(self,data , level):
        self.data = data
        self.level = level
    
def levelOrderlineweisePair(root):
    q = Queue()
    p = Pair(root , 1)
    q.push(p)
    level = 1
    while q.size() > 0:
        top = q.pop()
        if top.level > level : 
            level = top.level
            print()
        print(top.data.data , end = " ") # top.data = node of tree
        for i in top.data.children:
            p = Pair(i , level + 1)
            q.push(p)
    print()

def levelOrderzigzag(root):
    ms = Stack()
    ms.push(root)
    cs = Stack()
    level = 1
    while ms.size() > 0 : 
        node = ms.pop()
        print(node.data , end= " ")
        if level % 2 == 1:
            for i in node.children:
                cs.push(i)
        else :
            for i in range(len(node.children) -1 , -1 , -1):
                cs.push(node.children[i])
        if ms.size() == 0:
            ms = cs
            cs = Stack()
            level += 1
            print()  


if __name__ == "__main__":

    treedata = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100]
    s = Stack()
    root = None

    for i in treedata:
        if i == -1:
            s.pop()
        else :
            node = Node(i)
            if s.size() > 0 :
                peek = s.peek()
                peek.children.append(node)
                s.push(node)
            else : 
                root = node
                s.push(node)

    # levelOrder(root)
    # levelOrderlinewise(root)
    # levelOrderlinewisedelimieter(root)
    # levelOrderlinewiseCount(root)
    # levelOrderlineweisePair(root)
    levelOrderzigzag(root)
    
    # q = Queue()
    # q.push(10)
    # q.push(20)
    # q.push(30)
    # print(q.display())
    # print(q.pop())
    # print(q.display())
    # q.push(5)
    # print(q.display())
    


