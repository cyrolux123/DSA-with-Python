def numberOfDigits(n):
    
    if (n >= 1 and n <= 9):
        return 1
    elif (n == 0):
        return 0
    
    smallNum = int(n/10)
    smallAns =  numberOfDigits(smallNum)
    ans = 1 + smallAns
    return ans


print(numberOfDigits(12345))
print(numberOfDigits(234))