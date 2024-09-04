class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def middleElement(head):
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:   # before and faster and in if condition matters
        slow = slow.next
        fast = fast.next.next 
    print(slow.data)

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    middleElement(head)