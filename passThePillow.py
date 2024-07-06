class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos = 1
        dir = 1

        for i in range(1, time + 1):
            pos += dir
            if pos == 1:
                dir = 1
            elif pos == n:
                dir = -1
        return pos

# Main function to test the passThePillow method
def main():
    solution = Solution()
    
    # Test case 1
    n = 18
    time = 38
    print(solution.passThePillow(n, time))  # Expected output: 5

    # Test case 2
    n = 5
    time = 10
    print(solution.passThePillow(n, time))  # Expected output: 1

    # Additional test cases
    n = 3
    time = 4
    print(solution.passThePillow(n, time))  # Expected output: 2

    n = 4
    time = 7
    print(solution.passThePillow(n, time))  # Expected output: 2

if __name__ == "__main__":
    main()
