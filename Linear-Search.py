def linear_search(arr, target):

    size = len(arr)
    for index in range(size):
        if (arr[index] == target):
            return index
        
    return -1

my_list = [30, 20, 50, 40, 10, 60, 90]
target = 40

result = linear_search(my_list, target)
print("Element found at index: ", result)