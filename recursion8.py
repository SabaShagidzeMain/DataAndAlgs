# permutations(s): print all arrangements of the string.
# e.g. "abc" -> abc, acb, bca, cab, cba (3! = 6)

def permutations(current, remaining):

    if len(remaining) == 0:
        print(current)
        return
    
    for i in range(len(remaining)):
        char = remaining[i]

        new_remaining = remaining[:i] + remaining[i+1:]

        permutations(current + char, new_remaining)

permutations("", "abc")