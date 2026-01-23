class Node:
    def __init__(self, data):
        self.data=data
        self.next=None    
n1=Node(13)
n1.next= Node(14)
n1.next.next=Node(15)
n1.next.next.next= Node(16)
n1.next.next.next.next =Node(17)
search=int(input("Enter your seach: "))
temp=n1
while temp !=None:
    
    if temp.data==search:
        print("Find ")
        break   
    temp=temp.next




