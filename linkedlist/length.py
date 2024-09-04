class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    if head is None:
        return 0
    curr = head
    ans = 0
    while curr is not None:
        ans += 1
        curr = curr.next
    return ans

if __name__ == "__main__":
    head = Node(4)
    head.next = Node(3)
    head.next.next = Node(1)
    head.next.next.next = Node(5)
    ans = length(head)
    print(ans)