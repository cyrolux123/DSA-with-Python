def firstIndexOfElement(l1,x):

    if(len(l1)==0):
        return -1
    
    if(l1[0]==x):
        return 0
    
    ansFromRecursion = firstIndexOfElement(l1[1:],x)

    if(ansFromRecursion == -1):
        return ansFromRecursion
    else:
        return ansFromRecursion + 1



print(firstIndexOfElement([2, 3, 2, 4, 3, 5, 2],2))
print(firstIndexOfElement([2, 3, 2, 4, 3, 5, 2],3))
print(firstIndexOfElement([2, 3, 2, 4, 3, 5, 2],5))


def lastIndexOfElement(l1,x):
    
        if(len(l1)==0):
            return -1
        
        ansFromRecursion = lastIndexOfElement(l1[1:],x)
    
        if(ansFromRecursion == -1):
            if(l1[0]==x):
                return 0
            else:
                return -1
        else:
            return ansFromRecursion + 1
        
print(lastIndexOfElement([2, 3, 2, 4, 3, 5, 2],2))
print(lastIndexOfElement([2, 3, 2, 4, 3, 5, 2],3))
print(lastIndexOfElement([2, 3, 2, 4, 3, 5, 2],5))
        
