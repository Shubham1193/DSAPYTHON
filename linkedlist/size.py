class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


def sizeoflist(head):
    size = 0
    curr = head
    while curr != None:
        # print(curr.data)
        curr = curr.next
        size += 1
    return size



if __name__  == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    print("size of list is : " + str(sizeoflist(head)))