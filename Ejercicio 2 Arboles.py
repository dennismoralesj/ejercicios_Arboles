class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left= None
        self.right= None

def closest_value(root, tarjet):
    a = root.val
    kid = root.left if tarjet < a else root.right
    if not kid:
        return a 
    b = closest_value(kid, tarjet)
    return min((a,b), key= lambda x: abs(tarjet-x))

root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(8)
root.right.right = TreeNode(7)
root.right.right = TreeNode(24)
root.right.right.left = TreeNode(22)

result = closest_value(root, 19)
print(result)