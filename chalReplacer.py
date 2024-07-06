from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        def recursive(chalk, k):
            for i in range(len(chalk)):
                k -= chalk[i]
                if k < 0:
                    return i
            # Recur with the remaining k after one full cycle
            return recursive(chalk, k)
        
        # Reduce k by the total sum of chalk to minimize the number of full cycles
        k %= sum(chalk)
        
        return recursive(chalk, k)

# Main function to test the chalkReplacer method
def main():
    solution = Solution()
    
    # Test case 1
    chalk = [5, 1, 5]
    k = 22
    print(solution.chalkReplacer(chalk, k))  # Expected output: 0

    # Test case 2
    chalk = [3, 4, 1, 2]
    k = 25
    print(solution.chalkReplacer(chalk, k))  # Expected output: 1

    # Additional test cases
    chalk = [1, 2, 3]
    k = 7
    print(solution.chalkReplacer(chalk, k))  # Expected output: 0

    chalk = [2, 3, 4]
    k = 12
    print(solution.chalkReplacer(chalk, k))  # Expected output: 2

if __name__ == "__main__":
    main()
