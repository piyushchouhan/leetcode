nums = [2,3,1,3,2]

def frequencySort(nums):
        myMap = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in myMap:
                myMap[nums[i]] += 1
            else:
                myMap[nums[i]] = 1
        
        sorted_dict = sorted(myMap.items(), key=lambda item: (item[1], -item[0]))
        print(sorted_dict)

        result = []
        for key, value in sorted_dict:
            result.extend([key] * value)

        print(result)

frequencySort(nums)