def threeConsecutiveOdds(arr) -> bool:
        n = len(arr)
        count = 0
        for i in range(n-2):
            for j in range(i,i+3):
                if arr[j] % 2  == 1:
                    count += 1
            if count == 3:
                return True
            count = 0
        return False

arr = [2,6,4,1]
print(threeConsecutiveOdds(arr)) # False 