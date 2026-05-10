# Write a recursive function count_down(n) that prints numbers
# from n down to 1, then prints "Launch!"

def count_down(n):

    if n == 0:
        print("Launch!")
        return

    print(n)
    count_down(n - 1)

count_down(5)