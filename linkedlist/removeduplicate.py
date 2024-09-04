# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    

# def printlist(head):
#     curr = head
#     while curr != None:
#         print(curr.data , end = " - ") 
#         curr = curr.next
#     print()


# # def lastdata(head):
# #     curr = head
# #     while curr.next != None:
# #         curr = curr.next 
# #     return curr.data

# # def addlast(head , data):
# #     new_node = Node(data)
# #     curr = head
# #     while curr.next != None:
# #         curr = curr.next 
# #     curr.next = new_node
# #     return head

# # def removeduplicate(head):   # prev and curr or new list check with last
# #     ans = Node(head.data)
# #     curr = head
# #     while(curr != None):
# #         if curr.data == lastdata(ans):
# #             curr = curr.next
# #         else : 
# #             ans = addlast(ans ,curr.data)
# #             curr = curr.next

# def removeduplicate(head):
#     prev = head
#     curr = head.next
#     while curr != None:
#         if prev.data == curr.data:
#             curr = curr.next 
#         elif prev.data != curr.data:
#             prev.next = curr 
#             prev = prev.next
#             curr = curr.next 

#     return head

    
# if __name__ == "__main__" :
#     head = Node(2)
#     head.next = Node(2)
#     head.next.next = Node(2)
#     head.next.next.next = Node(3)
#     head.next.next.next.next = Node(3)
#     head.next.next.next.next.next = Node(4)
#     head.next.next.next.next.next.next = Node(5)
#     head.next.next.next.next.next.next.next = Node(5)
#     # printlist(head)
#     ans = removeduplicate(head)
#     printlist(ans)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

def printlist(head):
    curr = head
    while curr != None:
        print(curr.data, end=" - ") 
        curr = curr.next
    print()


def removeduplicate(head):
    prev = head
    curr = head.next
    while curr != None:
        if prev.data == curr.data:
            prev.next = curr.next  # Skip the duplicate node
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return head

    
if __name__ == "__main__":
    head = Node(2)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(3)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(5)
    head.next.next.next.next.next.next.next = Node(5)
    
    ans = removeduplicate(head)
    printlist(ans)
