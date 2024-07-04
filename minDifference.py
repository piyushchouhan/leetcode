import heapq
from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        min_four = sorted(heapq.nsmallest(4, nums))
        max_four = sorted(heapq.nlargest(4, nums))

        res = float("inf")
        for i in range(4):
            res = min(res, max_four[i] - min_four[i])
        
        return res

def main():
    solution = Solution()
    
    # Test cases
    nums1 = [5, 3, 2, 4]
    nums2 = [1, 5, 0, 10, 14]
    nums3 = [6, 6, 0, 1, 1, 4, 6]
    nums4 = [1, 5, 6, 14, 15]
    
    print("Test case 1:", solution.minDifference(nums1))  # Output: 0
    print("Test case 2:", solution.minDifference(nums2))  # Output: 1
    print("Test case 3:", solution.minDifference(nums3))  # Output: 2
    print("Test case 4:", solution.minDifference(nums4))  # Output: 1

if __name__ == "__main__":
    main()
