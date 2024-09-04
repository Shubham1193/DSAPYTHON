class Node:
    def __init__(self , new_data):
        self.data = new_data
        self.next = None


def insert_at_start(head , new_data):
    new_Node = Node(new_data)
    new_Node.next = head
    return new_Node


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    print_list(head)

    data = 1
    head = insert_at_start(head , data)
    print_list(head)
