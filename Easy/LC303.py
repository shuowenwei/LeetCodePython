# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/range-sum-query-immutable/

https://labuladong.github.io/algo/2/18/21/

LC303, LC304, LC560, LC528
"""
class NumArray(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.preSum = [0] * (len(nums) + 1)
        self.n = len(self.preSum)
        # self.preSum[i]: sum(nums[0:i]), [0,...,i), not include nums[i]
        for i in range(1, self.n):
            self.preSum[i] = nums[i-1] + self.preSum[i-1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # need nums[left] + nums[left + 1] + ... + nums[right], inclusive of left and right
        return self.preSum[right+1] - self.preSum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
