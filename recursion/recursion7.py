# generate_binary(n): print all n-character binary strings (using 0 and 1)
# e.g. n = 2 -> "00", "01", "10", "11"

def generate_binary(n, current = ""):

    if n == 0:
        print(current)
        return
    
    generate_binary(n - 1, current = "0")

    generate_binary(n - 1, current = "1")

generate_binary(3)