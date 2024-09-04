class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
    

def addlast(head ,data):

    if head == None:
        new_node = Node(data)
        return new_node

    new_node = Node(data)
    
    curr = head
    while(curr.next != None):
        curr = curr.next

    curr.next = new_node

    return head
    

def mergetwo(head1 , head2):
    
    res = None
    curr1 = head1
    curr2 = head2
    while(curr1 != None and curr2 != None):
        if curr1.data < curr2.data:
            res = addlast(res , curr1.data )   # error i have done is for the first node when res was empty then i have to capture that fisrt node  and then push to it
            curr1 = curr1.next
        elif curr2.data < curr1.data:
            res = addlast(res , curr2.data)
            curr2 = curr2.next

    while(curr1 != None):
        addlast(res , curr1.data)
        curr1 = curr1.next
    
    while(curr2 != None):
        addlast(res.curr2.data)
        curr2 = curr2.next
    
    return res

if __name__  == "__main__":
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)

    head2 = Node(2)
    head2.next = Node(4)
    ans = mergetwo(head1 , head2)
    while ans != None:
        print(ans.data)
        ans = ans.next