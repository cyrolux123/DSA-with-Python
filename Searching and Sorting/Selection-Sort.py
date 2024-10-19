def Selection_Sort(A):
    
    n = len(A)
    for i in range(n):
        min = i

        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j

        A[i], A[min] = A[min], A[i]
    return A

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = Selection_Sort(unsorted_list)
print("Sorted List: ", sorted_list)
