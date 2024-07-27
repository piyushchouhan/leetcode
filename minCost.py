def minCostToConvertString(source, target, original, changed, cost):
    n = len(source)
    if len(target) != n:
        return -1

    # Step 1: Create the cost mapping
    import collections
    import sys
    
    INF = sys.maxsize
    
    # Initialize the transformation cost dictionary
    transformation_costs = collections.defaultdict(lambda: INF)
    
    # Fill the initial transformation costs from original to changed with the given costs
    for i in range(len(original)):
        x, y, c = original[i], changed[i], cost[i]
        if transformation_costs[(x, y)] > c:
            transformation_costs[(x, y)] = c
    
    print(transformation_costs)
    
    # Step 2: Apply Floyd-Warshall to compute the minimum cost between any two characters
    characters = set(original + changed)
    print(characters)
    for k in characters:
        for i in characters:
            for j in characters:
                if transformation_costs[(i, k)] < INF and transformation_costs[(k, j)] < INF:
                    if transformation_costs[(i, j)] > transformation_costs[(i, k)] + transformation_costs[(k, j)]:
                        transformation_costs[(i, j)] = transformation_costs[(i, k)] + transformation_costs[(k, j)]

    print(transformation_costs)

    # Step 3: Calculate the total minimum cost to convert source to target
    total_cost = 0
    for i in range(n):
        if source[i] == target[i]:
            continue
        min_cost = transformation_costs[(source[i], target[i])]
        if min_cost == INF:
            return -1  # Transformation is not possible
        total_cost += min_cost
    
    return total_cost

def main():
    # Example input
    source = "abcd"
    target = "acbe"
    original = ["a","b","c","c","e","d"]
    changed = ["b","c","b","e","b","e"]
    cost = [2,5,5,1,2,20]
    
    result = minCostToConvertString(source, target, original, changed, cost)
    print(f"The minimum cost to convert source to target is: {result}")

if __name__ == "__main__":
    main()
