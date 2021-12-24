# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/car-pooling/

https://labuladong.gitee.io/algo/2/21/54/

LC370, LC1109, LC1094
"""
class Difference(object):
    def __init__(self, nums):
        # // 差分数组
        assert len(nums) > 0, 'Error, empty array'
        n = len(nums) 
        self.diff = [0] * n
        self.diff[0] = nums[0]
        for i in range(1, n):
            self.diff[i] = nums[i] - nums[i - 1]
        
    # /* 给闭区间 [i,j] 增加 val（可以是负数）*/
    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff): 
            self.diff[j+1] -= val
        # 当 j+1 >= diff.length 时，说明是对 nums[i] 及以后的整个数组都进行修改，那么就不需要再给 diff 数组减 val 了。

    # /* 返回结果数组 */
    def result(self):
        res = [0] * len(self.diff)
        # // 根据差分数组构造结果数组
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res
    
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        # since 0 <= fromi < toi <= 1000
        location = [0] * 1001
        diff = Difference(location)
        for val, i, j in trips:
            # // 即乘客在车上的区间是 [trip[1], trip[2] - 1]
            diff.increment(i, j-1, val)
        # print(diff.result())
        return max(diff.result()) <= capacity