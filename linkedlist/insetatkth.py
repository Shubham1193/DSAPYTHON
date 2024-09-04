class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


def insertPos(head,pos , data ,size):
    newNode = Node(data)
    if pos < 1 or pos > size + 1 :
        print("invalid pos")
        return head
    
    if pos == 1:
        newNode.next = head
        head = newNode
    else:
        curr = head
        for i in range(1,pos-1): #traverse just before 
            curr = curr.next  
        newNode.next = curr.next  # seq matters
        curr.next = newNode
    size += 1
    return head



def printList(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next
        print()

    
if __name__ == "__main__":
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(8)
    head.next.next.next = Node(4)

    size = 4
    # printList(head)

    data = 12
    pos = 3
    head = insertPos(head , pos , data , size)
    printList(head)