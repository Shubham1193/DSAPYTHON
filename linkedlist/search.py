class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def search(head , key):
    curr = head
    while curr is not None:
        if (curr.data == key):
            return 1
        else:
            curr = curr.next
    return 0

def searchRec(head , key):
    if head is None:
        return False
    if head.data == key:
        return True
    else:
        return searchRec(head.next , key)

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data , end=",")
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(4)
    head.next = Node(3)
    head.next.next = Node(1)
    head.next.next.next = Node(5)
    ans = search(head , 3)
    ansrec = searchRec(head , 3)
    print(ans)
    print(ansrec)
