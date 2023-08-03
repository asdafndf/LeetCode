# LeetCode problem 217: Contains Duplicate
# Return True if the list contains at least one duplicate
#--------------------------------------
nums = [1, 2, 3, 1]

def contains_duplicate(nums):
    return len(nums) != len(set(nums))


def contains_duplicate_v2(nums): # O(n^2), for loops
    length = len(nums)
    for num1 in range(length - 1):
        for num2 in range(num1 + 1, length):
            if nums[num1] == nums[num2]:
                return True
        

def contains_duplicate_v3(nums): # O(n*log(n))
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True


def contains_duplicate_v4(nums):
    nums_set = set()
    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)


def contains_duplicate_v5(nums):
    nums_map = {}
    for num in nums:
        if num in nums_map:
            return True
        nums_map[num] = nums_map.get(num, 0) + 1


#contains_duplicate(nums)
#contains_duplicate_v2(nums)
#contains_duplicate_v3(nums)
#contains_duplicate_v4(nums)
#contains_duplicate_v5(nums)


