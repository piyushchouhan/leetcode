# Description: This program creates an adjacency matrix from a list of edges of Directed Graph.
def create_adjacency_matrix(num_vertices, edges):
    # initialize the adjacency matrix with zeros
    adj_matrix= [[0]*num_vertices for _ in range(num_vertices)]

    # populate the adjacency matrix with the edge weights
    for edge in edges:
        src, dst = edge
        adj_matrix[src][dst] = 1 # 1 is the weight of the edge
    
    return adj_matrix


# Number of vertices
num_vertices = 4

# List of edges (src, dest)
edges = [(0, 1), (0, 2), (1, 2), (2, 3)]

# Create adjacency matrix
adj_matrix = create_adjacency_matrix(num_vertices, edges)

# Print the adjacency matrix
for row in adj_matrix:
    print(row)