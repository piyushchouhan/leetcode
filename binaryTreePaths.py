class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    def dfs(node, path, paths):
        if not node:
            return
        # Append current node value to the path
        path.append(str(node.val))
        # If it's a leaf node, append the path to paths list
        if not node.left and not node.right:
            paths.append('->'.join(path))
        else:
            # Continue to explore left and right subtrees
            dfs(node.left, path, paths)
            dfs(node.right, path, paths)
        # Backtrack to explore other paths
        path.pop()
    
    paths = []
    dfs(root, [], paths)
    return paths

# Helper function to build the tree for testing
def buildTree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    return root

# Testing the function
root = buildTree()
result = binaryTreePaths(root)
print(result)  # Output: ["1->2->5", "1->3"]
