# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

"""
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for n1, n2 in zip(self.nums, vec.nums):
            result += n1 * n2
        
        return result

