class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
       
n1=Node(12)
n2=Node(13)
n3=Node(14)

n1.next=n2
n2.next=n3
count=0
while n1!=None:
    count+=1
    n1=n1.next
print(f'Linght of Node is {count}')

