from collections import defaultdict

def findAncestors(n, edges):
    # Create adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    print(graph)
    
    # Create a list to store ancestors for each node
    ancestors = [set() for _ in range(n)]
    
    def dfs(node, ancestor):
        for neighbor in graph[node]:
            print(f"neigh : {neighbor}, {node}")
            if ancestor not in ancestors[neighbor]:
                ancestors[neighbor].add(ancestor)
                dfs(neighbor, ancestor)
    
    # Perform DFS from each node
    for node in range(n):
        dfs(node, node)
    
    # Convert sets to sorted lists
    sorted_ancestors = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
    
    return sorted_ancestors

# Example usage
n = 8
edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(findAncestors(n, edges))
