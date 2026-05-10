# digit_sum(n): sum all digits. e.g. digit_sum(1234) - 10
# Hint: n % 10 gives the last digit, n // 10 gives the rest

def digit_sum(n):

    if n == 0:
        return 0
    
    return (n % 10) + digit_sum(n // 10)

print(digit_sum(1234))