nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        res = target - n
        if res in d:
            return [d[res], i]
        else:
            d[n] = i





print(twoSum(nums, target))