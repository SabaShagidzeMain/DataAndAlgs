# is_palindrome(s): return True if string reads same forwards and backwards
# e.g. "abba" -> True, "hello" - False

def is_palindrome(s):

    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])

print(is_palindrome("abba"))
print(is_palindrome("hello"))