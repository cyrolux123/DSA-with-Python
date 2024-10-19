def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    
    last = fibonacci(n-1)
    secondLast = fibonacci(n-2)
    ans = last + secondLast
    return ans

print(fibonacci(5)) # Index is given as input 
    
