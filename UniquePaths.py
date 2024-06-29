def uniquePathsWithObstacles(grid):
    m = len(grid)
    n = len(grid[0])
    
    # Initialize a 2D DP array with all zeros
    dp = [[0] * n for _ in range(m)]
    
    # Base case: Start point
    dp[0][0] = 1 if grid[0][0] == 0 else 0
    
    # Fill the DP table
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
            else:
                dp[i][j] = 0
    
    # Return the number of unique paths to reach the bottom-right corner
    return dp[m-1][n-1]

# Example usage:
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

result = uniquePathsWithObstacles(grid)
print(f"Number of unique paths: {result}")
