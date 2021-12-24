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
        self.preSum = [0]*(len(nums)+1)
        # self.preSum[i] means sum(nums[0:i]), [0,...,i), not include nums[i]
        for i in range(1, len(nums)+1):
            self.preSum[i] = self.preSum[i-1] + nums[i-1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.preSum[right+1] - self.preSum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
