def print1ToN(n):
    if n == 0:
        return
    
    print1ToN(n-1)

    print(n)



print1ToN(5)