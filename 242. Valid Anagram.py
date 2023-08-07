# LeetCode problem 242: Valid Anagram
# Return True if s is an anagram of t
# ------------------------------------
from collections import defaultdict

s = "abcd"
t = "dcba"


def is_anagram(s, t): # O(n log(n)) due to sorting
    return sorted(s) == sorted(t)


def is_anagram_v2(s, t): 
    char_map = {}
    for char in s:
        char_map[char] = char_map.get(char, 0) + 1
    for char in t:
        char_map[char] = char_map.get(char, 0) - 1
    for value in char_map.values():
        if value != 0:
            return False
    return True


def is_anagram_v3(s, t): # Same idea as above with defaultdict
    char_count = defaultdict(int)
    for char in s:
        char_count[char] += 1
    for char in t:
        char_count[char] -= 1
    for value in char_count.values():
        if value != 0:
            return False
    return True
    

def is_anagram_v4(s, t):
    if len(s) != len(t): # Using a list not a hashmap
        return False
    char_count = [0] * 26
    for i in range(len(s)): # Iterating over two objects with the same length
        char_count[ord(s[i]) - ord("a")] += 1
        char_count[ord(t[i]) - ord("a")] -= 1
    for num in char_count:
        if num != 0:
            return False
    return True


#is_anagram(s, t)
#is_anagram_v2(s, t)
#is_anagram_v3(s, t)
#is_anagram_v4(s, t)


