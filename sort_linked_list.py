class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
def display(n1):
    temp= n1
    while temp is not None:
        print(temp.data, end="-->")
        temp =temp.next
    print(None)
def sort(head):
    
    while head is not None:
        j = head.next
        while j is not None:
            if head.data>j.data :
                temp=head.data
                
                head.data=j.data
                j.data=temp
            j=j.next
        head=head.next
n1=Node(2)
n2=Node(1)
n3=Node(5)
n4=Node(3)
n5=Node(4)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
print("Before sorting")
display(n1)
sort(n1)
print("After sorting")

display(n1) 




