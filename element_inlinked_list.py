# Print element of the linked list

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
n1=Node(12)
n1.next= Node(13)
n1.next.next=Node(14)
n1.next.next.next= Node(15)

while n1 != None:
    print(n1.data,"➡  ", end="")
    n1=n1.next

print("None")




