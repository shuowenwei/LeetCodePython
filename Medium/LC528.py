# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/random-pick-with-weight/

https://labuladong.gitee.io/algo/2/21/66/

LC303, LC304, LC560, LC528
"""
class Solution(object):
    
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.preSum = [0] * (len(w) + 1)
        self.n = len(self.preSum)
        for i in range(1, self.n):
            self.preSum[i] = self.preSum[i-1] + w[i-1]
        
    def pickIndex(self):
        """
        :rtype: int
        """
        import random
        target = random.randint(1, self.preSum[self.n - 1]) # // 在闭区间 [1, preSum[n - 1]] 中随机选择一个数字
        left, right = 0, self.n - 1
        while left <= right:
            mid = left + (right - left) / 2
            if self.preSum[mid] < target: 
                left = mid + 1
            elif self.preSum[mid] > target: 
                right = mid - 1
            elif self.preSum[mid] ==  target: 
                right = mid - 1 
        return left - 1 #  // preSum 的索引偏移了一位，还原为权重数组 w 的索引

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()