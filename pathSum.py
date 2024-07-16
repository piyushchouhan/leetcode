class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    def dfs(node, currentSum, path, paths):
        if not node:
            return
        # Append current node value to the path and update current sum
        path.append(node.val)
        currentSum += node.val
        # If it's a leaf node and the current sum equals targetSum, append the path to paths list
        if not node.left and not node.right and currentSum == targetSum:
            paths.append(list(path))
        else:
            # Continue to explore left and right subtrees
            dfs(node.left, currentSum, path, paths)
            dfs(node.right, currentSum, path, paths)
        # Backtrack to explore other paths
        path.pop()
    
    paths = []
    dfs(root, 0, [], paths)
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
result = pathSum(root, 8)
print(result)  # Output: [[1, 2, 5]]
