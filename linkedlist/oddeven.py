
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    

# def addlast(head , data):
#     new_node = Node(data)
#     if head == None:
#         return new_node
    
#     curr = head
#     while curr.next != None:
#         curr = curr.next
#     curr.next = new_node

# def oddeven(head):
#     even = None
#     odd = None
#     curr = head
#     while curr != None:
#         if curr.data % 2 == 0:
#             even = addlast(even , curr.data)
#         else :
#             odd = addlast(odd , curr.data)
#         curr = curr.next

#     ans = even
#     while even.next != None:
#         even = even.next 
#     even.next = odd

#     return ans

# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.data, end=" - ") 
#         curr = curr.next
#     print()


    
# if __name__ == "__main__":
#     head = Node(2)
#     head.next = Node(9)
#     head.next.next = Node(7)
#     head.next.next.next = Node(8)
#     head.next.next.next.next = Node(1)
#     head.next.next.next.next.next = Node(6)
#     head.next.next.next.next.next.next = Node(5)
#     head.next.next.next.next.next.next.next = Node(4)
#     ans = oddeven(head)
#     printlist(ans)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

def addlast(head , data):
    new_node = Node(data)
    if head == None:
        return new_node
    
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = new_node

def oddeven(head):
    even = None
    odd = None
    eventail = None 
    oddtail = None
    curr = head
    while curr.next != None:
        if curr.data % 2 == 0:
            if even == None:
                even = eventail = Node(curr.data)
            else :
                eventail.next = Node(curr.data)
                eventail = eventail.next
        else :
            if odd == None:
                odd = oddtail = Node(curr.data)
            else :
                oddtail.next = Node(curr.data)
                oddtail = oddtail.next
        curr = curr.next
    
    eventail.next = odd
    return even

def printlist(head):
    curr = head
    while curr != None:
        print(curr.data, end=" - ") 
        curr = curr.next
    print()


    
if __name__ == "__main__":
    head = Node(2)
    head.next = Node(9)
    head.next.next = Node(7)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(1)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(5)
    head.next.next.next.next.next.next.next = Node(4)
    ans = oddeven(head)
    printlist(ans)
    
    
    