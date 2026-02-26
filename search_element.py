class Treenode:
    def __init__(self,data):
        self.data =data
        self.left=None
        self.right=None

def search(node, value):
    if node is None:
        return

    if node.data == value:
        print("Value found: ",node.data)
    search(node.left, value)
    search(node.right, value)
    
root= Treenode(1)
root.left =Treenode(2)
root.right=Treenode(3)
value=int(input("Search element: "))
search(root,value)
        







