class TreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

t1=TreeNode(1)
t1.left=TreeNode(2)
t1.right=TreeNode(3)
print(t1.left.data)