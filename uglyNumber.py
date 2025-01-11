import heapq

def nthUglyNumber(n: int) -> int:
    # Min-heap to store the ugly numbers
    heap = [1]
    # Set to keep track of the unique ugly numbers
    seen = {1}
    # Multipliers corresponding to prime factors 2, 3, and 5
    factors = [2, 3, 5]
    
    ugly = 1
    for _ in range(n):
        # Extract the smallest number
        ugly = heapq.heappop(heap)
        
        # Generate the next set of ugly numbers
        for factor in factors:
            new_ugly = ugly * factor
            if new_ugly not in seen:
                seen.add(new_ugly)
                heapq.heappush(heap, new_ugly)
    
    return ugly

# Example usage:
n = 10
print(nthUglyNumber(n))  # Output should be 12
