def linear_search(arr, target):

    size = len(arr)
    for index in range(size):
        if (arr[index] == target):
            return index
        
    return -1

my_list = [10, 20, 30, 40, 50]
target = 40

result = linear_search(my_list, target)
print("Element found at index: ", result)