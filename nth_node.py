class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def display(head):
    temp = head
    while temp:
        print(temp.data, end="-->")
        temp = temp.next
    print("None")
def re_node(head, n):
    if n == 1:
        return head.next
    temp = head
    count = 1  
    while temp is not None and count < n - 1:
        temp = temp.next
        count += 1
    if temp is not None  and temp.next:
        temp.next = temp.next.next  
    return head
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print("Original List:")
display(head)
n = int(input("Which node to remove: "))
head = re_node(head, n)
print("Updated List:")
display(head)
