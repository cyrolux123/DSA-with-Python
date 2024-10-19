def factHead(n):
    if n == 0:
        return 1
    
    smallAns = factHead(n-1)
    ans = n * smallAns
    return ans

print(factHead(5))

'''
def factTailWrong(n):
    if n == 0:
        return 1
    return n * factTailWrong(n-1)
'''

def factTail(n, k = 1):
    if n == 0:
        return k
    
    k = n * k
    return factTail(n-1, k) 

print(factTail(5))