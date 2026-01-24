class Node:
    def __init__(self, data):
        self.data= data
        self.prev= None
        self.next=None
n1=Node(12)
n2=Node(13)
n3=Node(14)
n4=Node(15)
n1.next=n2
n2.next=n3
n3.next =n4
n2.prev= n1
n3.prev=n2
n4.prev=n3
temp=n1
while temp is not None:
    print(temp.data,"-->",end="")
    temp=temp.next
print("None")
temp=n4
while temp:
    print(temp.data,"-->",end="")
    temp=temp.prev

print("None")



