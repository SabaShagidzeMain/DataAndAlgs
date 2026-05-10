# power(base, exp): compute base^exp. Try the O(log n) fast version!

def power(base, exp):

    if exp == 0:
        return 1
    
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    
    return base * power(base, exp - 1)

print(power(2, 10))