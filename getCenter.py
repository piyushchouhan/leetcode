array = [[1,2],[5,1],[1,3],[1,4]]
n = len(array)

flattened_list = [element for sublist in array for element in sublist]

print(flattened_list)

my_map = {}

for i in flattened_list:
    if i in my_map:
        my_map[i] += 1
    else:
        my_map[i] = 1

for key, value in my_map.items():
    if value == n:
        print(key)
        break

print(my_map)