def powerTwo(n):
    if (n == 1): # Base case
        return 2
    
    smallAns = powerTwo(n-1) # Induction Hypothesis
    ans = 2 * smallAns # Induction Step
    return ans 







print(powerTwo(5))