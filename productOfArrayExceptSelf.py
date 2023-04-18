nums = [1,2,3,4]

# def productofArrayExceptSelf(nums):
#     product = 1
#     res = []
#     for n in nums:
#         product *= n
#     for n in nums:
#         res.append(product/n)
#     return int(res) - just division solution but mentioned in the question that this cannot be used.


# original=[1, 2, 3, 4]
# prefix = 6
# postfix = 24

# output = [24,12,8,6]

def productofArrayExceptSelf(nums):
    prefix = 1
    output = [1] * len(nums)
    for i in range(len(nums)):
        output[i] = prefix
        print(output)
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]
    return output

        


print(productofArrayExceptSelf(nums))
