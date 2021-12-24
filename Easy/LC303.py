# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/range-sum-query-immutable/

https://labuladong.gitee.io/algo/2/21/53/

LC303, LC304, LC560
"""
class NumArray(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.preSum = {-1: 0}
        for i, val in enumerate(nums):
            self.preSum[i] = self.preSum[i-1] + val

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.preSum[right] - self.preSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
