class Node:
    def __init__(self , data):
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
    
def display(root):
    print("node" , end=" ")
    print(root.data)
    for i in root.children:
        print("Edge" , end= " ")
        print(root.data , i.data)
        display(i)
    print("post " , end=" ")
    print(root.data)

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
    display(root)