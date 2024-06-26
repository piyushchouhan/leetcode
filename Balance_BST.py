class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    inorder(root)
    return result

def sorted_list_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_list_to_bst(nums[:mid])
    root.right = sorted_list_to_bst(nums[mid+1:])
    return root

def balanceBST(root):
    sorted_values = inorder_traversal(root)
    return sorted_list_to_bst(sorted_values)


# Helper function to print the tree in pre-order for verification
def preorder_traversal(root):
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

# Example usage
root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
balanced_root = balanceBST(root)
print(preorder_traversal(balanced_root))  # Output should be a balanced BST's pre-order traversal
