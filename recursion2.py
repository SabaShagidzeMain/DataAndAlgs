# Write factorial(n) recursively. Handle n=0 and n=1 as base cases

def factorial(n):

    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))