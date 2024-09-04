class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def size(head):
    curr = head
    size = 0
    while curr is not None:
        curr = curr.next 
        size += 1
    return size

def getNodeAt(head , pos):
    curr = head
    for i in range(1,pos):
        curr = curr.next
    return curr

def reverselist(head):
    left = 1
    right = size(head)
    while(left <= right):
        leftNode = getNodeAt(head , left)
        rightNode = getNodeAt(head , right)
       
        temp = leftNode.data
        leftNode.data = rightNode.data
        rightNode.data = temp
        left += 1
        right -=1

def printlist(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    reverselist(head)
    printlist(head)
    