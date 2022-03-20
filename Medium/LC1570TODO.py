# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

https://goodtecher.com/leetcode-1570-dot-product-of-two-sparse-vectors/

"""
# class SparseVector:
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec: 'SparseVector') -> int:
#         result = 0
#         for n1, n2 in zip(self.nums, vec.nums):
#             result += n1 * n2
#         return result

class SparseVector(object):
    def __init__(self, nums):
        self.dict_index2num = {}
        for i, n in enumerate(nums):
            if n != 0 : 
                self.dict_index2num[i] = n
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        res = 0
        for index, val in self.dict_index2num.items():
            res += self.dict_index2num[index] * vec.dict_index2num.get(index, 0)
        return res

# nums1 = [1,0,0,2,3]
# nums2 = [0,3,0,4,0]
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# print(v1.dotProduct(v2))