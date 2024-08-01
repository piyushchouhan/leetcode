import heapq

def networkDelayTime(times, n, k):
    # Create the adjacency list
    graph = {i: [] for i in range(1, n+1)}
    for u, v, w in times:
        graph[u].append((v, w))

    print(f"Graph: {graph}")
    
    # Priority queue to hold the (time, node)
    min_heap = [(0, k)]
    # Dictionary to hold the shortest time to reach each node
    shortest_time = {i: float('inf') for i in range(1, n+1)}
    shortest_time[k] = 0
    print(f"Shortest time: {shortest_time}")
    print(f"Min heap: {min_heap}")
    
    while min_heap:
        current_time, u = heapq.heappop(min_heap)
        # If the current node's time is greater than the recorded shortest time, skip it
        if current_time > shortest_time[u]:
            continue
        
        for v, w in graph[u]:
            time = current_time + w
            if time < shortest_time[v]:
                shortest_time[v] = time
                heapq.heappush(min_heap, (time, v))
    
    # Get the maximum time from the shortest_time dictionary
    max_time = max(shortest_time.values())
    
    # If any node is unreachable, return -1
    return max_time if max_time < float('inf') else -1

# Example usage
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))  # Output: 2
