class Node: 
    def __init__(self, data):
        self.data= data
        self.next=None
def insert(head,data):
    new = Node(data)
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
def re_duplicate(head):
    dup=head
    while dup is not None:
        re_dup=dup
        while re_dup.next is not None:
            if re_dup.next.data==dup.data:
                re_dup.next=re_dup.next.next
            else:
                re_dup=re_dup.next
        dup=dup.next
    return head
n1=int(input("Enter the number of nodes: "))
head=None
for i in range(n1):
    val=int(input("Enter element: "))
    head=insert(head,val)
display(head)
head=re_duplicate(head)
print("After removing duplicates:")
display(head)



