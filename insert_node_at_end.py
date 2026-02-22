class Node:
    def __init__(self, data):
        self.data= data
        self.next=None

def insert_end(head, data):
    new=Node(data)
    if head is None:
        return new
    temp=head
    while temp.next is not None:
        temp=temp.next
    temp.next=new
    return head
def display(head):
    temp=head
    while temp is not None:
        print(temp.data,end="-->")
        temp=temp.next
    print(None)

n=int(input("Enter the number oof node: "))
head=None
for i in range(n):
    val=int(input("Enter the element: "))
    head=insert_end(head, val)

display(head)

