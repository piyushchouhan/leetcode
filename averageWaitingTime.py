customers = [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]
m = len(customers)

flattenArray = [element for row in  customers for element in row]

print(flattenArray)
n = len(flattenArray)


ptr1 = 0
ptr2 = 1

Sum = flattenArray[0]
totalSum = 0

while ptr2 < n:
    if Sum < flattenArray[ptr1]:
        totalSum += flattenArray[ptr2]
    else:
        Sum += flattenArray[ptr2]
        totalSum += (Sum - flattenArray[ptr1])
    ptr1 += 2
    ptr2 += 2

print(totalSum/m)