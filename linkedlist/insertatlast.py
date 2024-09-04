class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

def insertAtEnd(head , new_data):
    new_Node = Node(new_data)

    # if the list is empty
    if head is None:
        return new_Node
    
    last = head
    while last.next:
        last = last.next
    
    last.next = new_Node

    return head

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head = insertAtEnd(head , 9)
    printList(head)