# Create a linked list and count how many nodes it has.

class My_node:
    def __init__(self,data):
        self.data= data
        self.next= None
n1 = My_node(50)
n2= My_node(40)
n3 = My_node(30)
node4 = My_node(20)

n1.next = n2
n2.next= n3
n3.next= node4

count= 0
temp=n1
while temp != None:
    count+= 1
    temp=temp.next
print(f'Count is {count}')

















