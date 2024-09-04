class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# 2 approach 2pointer and size

def kthelement(head , pos):
    slow = head
    fast = head
    for i in range(pos):
        fast = fast.next 
    # print(fast.data)

    while fast != None:
        print(slow.data)
        print(fast.data)
        slow = slow.next
        fast = fast.next
        
    
    print(slow.data) # 3 ka diff slow at 1 fast at 4 and end mae fast at none and slow at 3

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    kthelement(head , 3)