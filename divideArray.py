class Solution:
    def divideArray(self, nums) -> bool:
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        for count in count_map.values():
            if count % 2 != 0:
                return False

        return True

# Main function to test the divideArray method
def main():
    solution = Solution()
    
    # Test case 1
    nums = [3, 2, 3, 2, 2, 2]
    print(solution.divideArray(nums))  # Expected output: True

    # Test case 2
    nums = [1, 2, 3, 4]
    print(solution.divideArray(nums))  # Expected output: False
    
    # Additional test cases
    nums = [4, 4, 1, 1, 2, 2]
    print(solution.divideArray(nums))  # Expected output: True

    nums = [1, 1, 1, 1, 2, 2, 2, 2]
    print(solution.divideArray(nums))  # Expected output: True