# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/partition-equal-subset-sum/

https://labuladong.gitee.io/algo/3/25/82/
0/1 backpacking
LC416
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumNums = sum(nums)
        if sumNums % 2 == 1:
            return False
        sumNums = sumNums / 2 
        dp_table = [ [False]* (sumNums+1) for _ in range(len(nums)+1) ] # dp[0...len(nums)-1][0...sumNums-1]
        
        # 由于 i 是从 1 开始的，而数组索引是从 0 开始的，所以第 i 个物品的重量应该是 nums[i-1]，这一点不要搞混。
        for i in range(len(nums)+1):
            dp_table[i][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, sumNums+1):
                if j < nums[i-1]:
                    # // 背包容量不足，不能装入第 i 个物品
                    dp_table[i][j] = dp_table[i-1][j] 
                else:
                    # // 装入或不装入背包
                    # 如果 j - nums[i-1] 的重量可以被恰好装满，那么只要把第 i 个物品装进去，也可恰好装满 j 的重量；否则的话，重量 j 肯定是装不满的。
                    dp_table[i][j] = dp_table[i-1][j] or dp_table[i-1][j-nums[i-1]]
                
        return dp_table[len(nums)][sumNums]