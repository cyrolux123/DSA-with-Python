def printNTo1(n):
    if n <= 0:
        return
    
    print(n)
    printNTo1(n-1)

printNTo1(5)