def checkSorted(l1):
    if (len(l1) == 0 or len(l1) == 1):
        return True
    
    ans = checkSorted(l1[1:])

    if(l1[0] < l1[1]):
        return ans
    else:
        return False



print(checkSorted([2,1,3,4,5,6,7,8,9,10])) 