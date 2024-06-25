class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertBST(root: TreeNode) -> TreeNode:
    def reverse_inorder(node, acc_sum):
        if not node:
            return acc_sum
        acc_sum = reverse_inorder(node.right, acc_sum)
        node.val += acc_sum
        acc_sum = node.val
        acc_sum = reverse_inorder(node.left, acc_sum)
        return acc_sum

    reverse_inorder(root, 0)
    return root

# Create an object of TreeNode
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(15)

# Convert BST to Greater Tree
new_root = convertBST(root)
print(new_root) 