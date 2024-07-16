class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLCA(root, n1, n2):
    if not root or root.val == n1 or root.val == n2:
        return root
    left = findLCA(root.left, n1, n2)
    right = findLCA(root.right, n1, n2)
    if left and right:
        return root
    return left if left else right

def findPath(root, value, path):
    if not root:
        return False
    if root.val == value:
        return True
    path.append('L')
    if findPath(root.left, value, path):
        return True
    path.pop()
    path.append('R')
    if findPath(root.right, value, path):
        return True
    path.pop()
    return False

def getDirections(root, startValue, destValue):
    lca = findLCA(root, startValue, destValue)
    
    startPath = []
    destPath = []
    
    findPath(lca, startValue, startPath)
    findPath(lca, destValue, destPath)
    
    # Convert startPath to 'U'
    upPath = ['U'] * len(startPath)
    
    # Combine paths
    return ''.join(upPath) + ''.join(destPath)

# Helper function to build the tree for testing
def buildTree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

# Testing the function
root = buildTree()
startValue = 4
destValue = 6
directions = getDirections(root, startValue, destValue)
print(f"Directions from {startValue} to {destValue}: {directions}")
