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
    

    
def mirror(root):
    for i in root.children:
        mirror(i)
    root.children = list(reversed(root.children))

def printlinewise(root):
    q = Queue()
    q.push(root)
    q.push(Node(-1))
    while q.size() > 0:
        data = q.pop()
        if data.data == -1: # think of tree like 10 child 20 30 40 ... so 10 -1 ... 10 pop 20 30 40 push in queue -1 pop prinline and -1 pushagain 20 30 40 pop then [-1] 
            # pop -1 println and agin push -1 so this keeps on
            if q.size() > 0:
                print()
                q.push(Node(-1))
        else:
            print(data.data , end = " ")
            for i in data.children:
                q.push(i)
    print()

def removeleaves(root):
    temp = []
    for i in root.children:
        if len(i.children) != 0:
            temp.append(i)
    root.children = temp

    for i in root.children:
        removeleaves(i)

def findinGenerictree(root , data):
    if root.data == data:
        return True
    for i in root.children:
        fic = findinGenerictree(i , data)
        if fic == True:
            return True
    return False

def nodetoRootpath(root, data):
    route = []
    
    # Check if the root node itself contains the data
    if root.data == data:
        route.append(root.data)
        return route
    
    # Explore all children recursively
    for i in root.children:
        routeofchild = nodetoRootpath(i, data)
        
        # If a path is found in the child, add the current root's data and return
        if len(routeofchild) > 0:
            routeofchild.append(root.data)
            return routeofchild
    
    # If no path is found, return an empty list
    return route

# ask chatgpt to write comment
def lowestCommonAncestor(root , data1 , data2):
    path1 = nodetoRootpath(root , data1)
    path2 = nodetoRootpath(root , data2)
    i = len(path1) -1
    j = len(path2) - 1
    while(i >= 0 and j >= 0 and path1[i] == path2[j]):
        i -= 1
        j -= 1
    i += 1
    j += 1
    return path1[i]

def distanceBetweenNodes(root , data1 , data2):
    path1 = nodetoRootpath(root , data1)
    path2 = nodetoRootpath(root , data2)
    i = len(path1) - 1
    j = len(path2) - 1
    while i >= 0 and j >= 0 and path1[i] == path2[j]:
        i -= 1
        j -= 1
    i += 1
    j += 1
    return i + j

def areTreesimilar(root, root1):
    # Check if the number of children in both roots is the same
    if len(root.children) != len(root1.children):
        return False
    
    # Compare children recursively
    for i in range(0, len(root.children)):
        c1 = root.children[i]  # for 20 and 27
        c2 = root1.children[i]
        
        # Recursively check if the subtrees rooted at these children are similar
        if not areTreesimilar(c1, c2):
            return False
    
    return True

def areTreemirror(root , root1):
    if len(root.children) != len(root1.children):
        return False

    for i in range(0 , len(root.children)):
        j = len(root.children) - 1 - i
        c1 = root.children[i]   
        c2 = root1.children[j]
        if not areTreemirror(c1 , c2):
            return False

    return True

class MultisolverClass : 
    size = 0
    max = -1
    min = 10000
    height = -1 # in edges

    def multisolver(self , root , depth):
        self.size += 1
        self.min = min(root.data , self.min)
        self.max = max(root.data , self.max)
        self.height = max(self.height , depth)
        for i in root.children:
            self.multisolver(i , depth + 1)



if __name__ == "__main__":

    treedata = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100]
    treedata2 = [2,27,10,-1,6,-1,-1,32,12,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100]
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

    s = Stack()
    root1 = None

    for i in treedata2:
        if i == -1:
            s.pop()
        else :
            node = Node(i)
            if s.size() > 0 :
                peek = s.peek()
                peek.children.append(node)
                s.push(node)
            else : 
                root1 = node
                s.push(node)
   
    
    # print("normal")         
    printlinewise(root)
    # printlinewise()
    # mirror(root)
    # print("mirrored")
    # removeleaves(root)
    # printlinewise(root)
    # print(findinGenerictree(root , 180))
    # print(nodetoRootpath(root , 110))
    # print(lowestCommonAncestor(root , 100 , 110))
    # print(distanceBetweenNodes(root , 70 , 110 ))
    # print(areTreesimilar(root , root1))
    # print(areTreemirror(root , root1))
    # print(size, max, min , height)
    # multisolver(root , -1)
    # print(size, max, min , height)
    m = MultisolverClass()
    m.multisolver(root , -1)
    print(m.height , m.size  , m.max , m.min)