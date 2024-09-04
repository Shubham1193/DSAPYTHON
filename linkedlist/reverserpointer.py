class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

def reversepointer(head):
    prev = None
    curr = head
    
    while curr is not None:
        temp = curr.next    # pointer save then move pointer else loose
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

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
    curr = reversepointer(head)
    printlist(curr)
    # print(curr.data)