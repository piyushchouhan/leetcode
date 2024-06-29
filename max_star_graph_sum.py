from collections import defaultdict
from termcolor import cprint

vals = [1, -8, 0]
edges = [[1, 0], [2, 1]]
k = 2

n = len(vals)

# Step 1: Create an adjacency list
adj_list = defaultdict(list)
for a, b in edges:
    adj_list[a].append(b)
    adj_list[b].append(a)

print("Adjacency list before sorting:")
print(adj_list)

# Step 2: Sort neighbors in descending order by value
for node in adj_list:
    adj_list[node].sort(key=lambda x: vals[x], reverse=True)

print("Adjacency list after sorting:")
print(adj_list)

# Step 3: Calculate the maximum star graph sum with the immediate positive sum condition
max_sum = float('-inf')
for node in range(n):
    # Take the value of the node itself
    current_sum = vals[node]
    # Add the values of up to k highest-valued neighbors
    immediate_positive = False
    for neighbor in adj_list[node][:k]:
        if vals[neighbor] >= 0:
            immediate_positive = True
        cprint(f"{neighbor}: {vals[neighbor]}", "green")
        current_sum += vals[neighbor]
    
    # If an immediate positive sum is found, use it
    if immediate_positive and current_sum > 0:
        max_sum = max(max_sum, current_sum)
    # Otherwise, keep the maximum sum found
    else:
        max_sum = max(max_sum, vals[node])

print("Maximum star graph sum:")
print(max_sum)
