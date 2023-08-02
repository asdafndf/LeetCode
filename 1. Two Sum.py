# LeetCode problem 1: Two Sum
# Given an array of integers return the indices of two numbers that adds up to target
#--------------------------
lst = [2, 7, 11, 15]
target = 26

def two_sum(lst):
    for num1 in lst:
        for num2 in lst:
            if num1 + num2 == target:
                return [lst.index(num1), lst.index(num2)]
          
            
def two_sum_v2(lst):
    i1 = 0
    i2 = 1
    total = 0
    while i1 < len(lst):
        while i2 < len(lst):
            if lst[i1] + lst[i2] == target:
                return [i1, i2]
            i2 += 1
        i1 += 1
        i2 = i1 + 1


def two_sum_v3(nums):
    map = {}
    for index, num in enumerate(nums):
        if (target - num) in map:
            return [index, map[target - num]]
        map[num] = index

#two_sum(lst)
#two_sum_v2(lst)
#two_sum_v3(lst)


