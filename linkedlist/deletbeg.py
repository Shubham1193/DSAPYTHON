class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

def deleteBeg(head):
    if not head:
        print("List is empty, nothing to delete.")
        return head  # Empty list

    # Move head to the next node
    new_head = head.next
    head = None  # Free memory of the old head
    return new_head

def deleteEnd(head):
    curr = head

    perv = None
    while curr.next is not None:
        prev = curr
        curr = curr.next
    
def deleteAt(head , pos):
    curr = head
    for i in range(1 , pos-1):
        curr = curr.next
    curr.next = curr.next.next
    return curr

def deleteAtt(head , pos):
    prev = None
    curr = head
    for i in range(1 , pos):
        prev = curr
        curr = curr.next
    prev.next = curr.next
    curr.next = None
    # curr.next = curr.next.next
    return prev

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    printList(head)
    delAt = deleteAtt(head , 2)

    # head = deleteBeg(head)
    printList(delAt)