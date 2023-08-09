"""
Leetcode problem 2357: Make Array Zero by Subtracting Equal Amounts
Return the minimum number of operations to make the list all zeros,
by substracting the smallest non-zero element always.
"""
nums = [1, 5, 0, 3, 5]


def minimum_operations(nums):
    count = 0
    while sum(nums) != 0:
        nums_2 = []
        for num in nums:
            if num != 0:
                nums_2.append(num)
        for i, num in enumerate(nums):
            if num != 0:
                nums[i] -= min(nums_2)
        nums_2.clear()
        count += 1
    return count


def minimum_operations_v2(nums): # each unique number except 0 needs 1 operation
    set_nums = set(nums)
    length = len(set_nums)
    if 0 in set_nums:
        return length - 1
    return length


#minimum_operations(nums)
#minimum_operations_v2(nums)



