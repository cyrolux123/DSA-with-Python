def sumArray(arr):
    if (len(arr) == 0):
        return 0
    
    sumOfLeftOverArray = sumArray(arr[1:])
    ans = arr[0] + sumOfLeftOverArray
    return ans


def sumArray2(arr):
    if (len(arr) == 0):
        return 0
    
    ans = arr[0] + sumArray2(arr[1:])

    return ans


def sumArrayTail(arr,k = 0):
    if (len(arr) == 0):
        return k
    
    k = k + arr[0]
    ans = sumArrayTail(arr[1:],k)

    return ans


print(sumArray([1,2,3,4,5]))
print(sumArray([]))
print(sumArray2([1,2,3,4,5]))
print(sumArray2([]))
print(sumArrayTail([1,2,3,4,5]))
print(sumArrayTail([]))
