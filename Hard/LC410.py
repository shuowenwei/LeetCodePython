# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/split-array-largest-sum/

https://labuladong.gitee.io/algo/2/21/63/
https://mp.weixin.qq.com/s/E2cyJwMVxRosaU2-bZyTjA

LC704, LC34, LC875, LC1101, LC410
"""
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # /* 辅助函数f(x)，若限制最大子数组和为 max，
        # 计算 nums 至少可以被分割成几个子数组 */
        def splitArray(nums, maxSum):
            count = 1 # // 至少可以分割的子数组数量
            sectionSum = 0 # // 记录每个子数组的元素和
            for i in range(len(nums)):
                if nums[i] + sectionSum > maxSum:
                    count += 1 
                    sectionSum =  nums[i]
                else:
                    sectionSum += nums[i]
            return count
        
        low = max(nums)
        high = sum(nums)
        # find left boundary
        while low <= high: 
            mid = low + (high - low)/2 
            n = splitArray(nums, mid)
            if n == m:
                high = mid - 1
            elif n < m: 
                high = mid - 1
            elif n > m: 
                low = mid + 1 
        return low 