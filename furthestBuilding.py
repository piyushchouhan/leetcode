import heapq

def furthestBuilding(heights, bricks, ladders):
    heap = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff > 0:
            heapq.heappush(heap, diff)
        if len(heap) > ladders:
            bricks -= heapq.heappop(heap)
        if bricks < 0:
            return i
    return len(heights) - 1

# Example usage:
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
print(furthestBuilding(heights, bricks, ladders))  # Output: 4