nums = [1,2,3,4,5,6]

def containsDuplicate(nums):
    d = {}
    for n in nums:
        if n in d:
            return True
        else:
            d[n] = 1
    return False

print(containsDuplicate(nums))