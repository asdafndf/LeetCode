# LeetCode problem 9: Palindrome number
# Determine whether a number is a palindrome
#----------------------
x = 1234321

def is_palindrome_v1(x):
    return str(x) == str(x)[::-1]


def is_palindrome_v2(x):
    original_number = x
    reversed_number = 0
    while x > 0:
        reversed_number = reversed_number * 10 + x%10
        x //= 10
    return original_number == reversed_number


def is_palindrome_v3(x):
    if (x < 0) or (x%10 == 0):
        return False
    
    result = 0
    while x > result:
        result = result * 10 + x%10
        x //= 10
    return x == result or x == result // 10


#is_palindrome_v1(x)
#is_palindrome_v2(x)
#is_palindrome_v3(x)


