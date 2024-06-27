vals = [1,2,3,4,10,-10,-20]
edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]]
k = 2

from collections import defaultdict
    
n = len(vals)

# Step 1: Create an adjacency list
adj_list = defaultdict(list)
for a, b in edges:
    adj_list[a].append(b)
    adj_list[b].append(a)

# step 2 = sort neighbors in descending order by value
for node in adj_list:
            adj_list[node].sort(key=lambda x: vals[x], reverse=True)


 # Step 3: Calculate the maximum star graph sum
max_sum = float('-inf')
for node in range(n):
    # Take the value of the node itself
    current_sum = vals[node]
    # Add the values of up to k highest-valued neighbors
    for neighbor in adj_list[node][:k]:
        current_sum += vals[neighbor]
    
    # Update the maximum sum found
    max_sum = max(max_sum, current_sum)

print(max_sum)