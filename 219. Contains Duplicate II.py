# LeetCode problem 219: Contains Duplicate II
# Return True if two duplicates are sufficiently close (k) to each other
# ----------------------------
nums = [1, 2, 3, 1, 4, 5]
k = 2


def contains_nearby_duplicate(nums, k):
    for i1 in range(len(nums) - 1):
        start = i1 + 1
        try:
            for i2 in range(start, start + k):
                if nums[i1] == nums[i2]:
                    return True
        except IndexError:
            continue
        

def contains_nearby_duplicate_v2(nums, k):
    nums_map = {}
    for i in range(len(nums)):
        if nums[i] in nums_map:
            if abs(nums_map[nums[i]] - i) <= k:
                return True
            nums_map[nums[i]] = i
        nums_map[nums[i]] = i


#contains_nearby_duplicate(nums, k)
#contains_nearby_duplicate_v2(nums, k)


