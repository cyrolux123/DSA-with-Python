def insertion_sort(A):
    
    n = len(A)

    for i in range(1, n):
        temp = A[i]
        j = i - 1

        while ( j >= 0 and A[j] > temp):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = temp
    return A

unsorted_array = [5, 2, 4, 6, 1, 3]
sorted_array = insertion_sort(unsorted_array)
print(sorted_array)