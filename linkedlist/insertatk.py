class Node :
    def __init__(self , data):
        self.data = data
        self.next = None
    

def insertAtK(head , new_data , pos):
    curr = head
    if pos == 1 : 
        new_node = Node(new_data)
        new_node.next = head
        return head
    for i in range(1 , pos-1):    # 3 1 2 
        curr = curr.next
    new_node = Node(new_data)
    new_node.next = curr.next
    curr.next = new_node





def print_list(head):
    curr = head
    while(curr != None):
        print(curr.data)
        curr = curr.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    insertAtK(head , 3 , 3)
    print_list(head)