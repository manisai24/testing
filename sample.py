# harmonic series using recursion
 
def sum(n):
 
    # Base condition
    if n < 3:
        return 1
 
    else:
        return 1 / n + (sum(n - 2))
         
print(sum(9))