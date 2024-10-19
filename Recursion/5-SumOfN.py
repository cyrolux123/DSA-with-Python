def SumOfNumbersTillN(n):
    if(n == 1): # Base case
        return 1
    
    smallAns = SumOfNumbersTillN(n-1) # Assumption
    ans = n + smallAns # Induction
    return ans


print(SumOfNumbersTillN(5))
print(SumOfNumbersTillN(10))
