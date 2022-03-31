

nums = [2,3,4,5,7]

# def countSubset(nums, K):
#     nums.sort() 
#     res = 0
#     right = len(nums) - 1
#     while right > 0:
#         for i in range(0, right):
#             if nums[i] >= K - nums[right]: # subset's largest number is nums[right] 
#                 break 
#         print(nums[right], i, 2**(i + 1))
#         if i > 0:
#             res += 2**(i + 1)
#         elif i == 0 and nums[right] * 2 < K:
#             res += 1
#         right -= 1
#     return res 

nums = [2,3,4,5,7]
K = 8 
print(countSubset(nums, K))

# time: O(n^2) -> O(nlog(n))
# space: O(1)


def countSubset2Pointers(nums, K):
    n = len(nums)
    nums.sort() 
    left = 0
    right = len(nums) - 1
    res = 0 
    for i in range(n):
        for j in range(i, n):
            if nums[i] + nums[j] < K:
                res += 2 ** (max(j - i - 1, 0))
    return res
print(countSubset2Pointers(nums, K))

            