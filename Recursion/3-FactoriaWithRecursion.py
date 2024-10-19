'''import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(200)
print(sys.getrecursionlimit())'''

def factorial(n):
    if n == 1: # Base case
        return 1
    return n * factorial(n-1)

print(factorial(5))


'''
def factorial(n):
    return n * factorial(n-1)

def factorialFour(n):
    return n * factorialThree(n-1)

def factorialThree(n):
    return n * factorialTwo(n-1)

def factorialTwo(n):
    return n * factorialOne(n-1)

def factorialOne(n):
    return 1
'''