# Array must be sorted

def binary_search(arr, target):

    size = len(arr)
    start = 0
    end = size - 1

    while (start <= end):
        mid = (start + end) // 2
        if (arr[mid] == target):
            return mid
        
        if (arr[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
    
    

sorted_list = [10, 20, 30, 40, 50, 60]
target = 40

result = binary_search(sorted_list, target)
print("Element found at index: ", result)