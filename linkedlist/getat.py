class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


def dataAt(head , pos):
    curr = head
    for i in range(1, pos):
        curr = curr.next
    return curr.data

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    print(dataAt(head,2))