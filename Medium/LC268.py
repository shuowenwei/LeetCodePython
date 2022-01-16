# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/missing-number/

https://labuladong.gitee.io/algo/4/30/120/

LC172, LC793, LC204, LC372, LC268
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use Sum = (length+1)*length/2
        length = len(nums)
        return (0+length)*(length+1)/2 - sum(nums)

        # solution 2: 
        """
        # 对于异或运算（^），我们知道它有一个特殊性质：
        # 一个数和它本身做异或运算结果为 0，一个数和 0 做异或运算还是它本身。
        # 2^3^2 = 3^(2^2) = 3^0 = 3 
        n = len(nums)
        res = 0
        res ^= n # // 先和新补的索引异或一下
        for i in range(len(nums)):
            # 只要把所有的元素和索引做异或运算，成对儿的数字都会消为 0，只有这个落单的元素会剩下
            res ^= i ^ nums[i] 
        return res 
        """
        
        # solution 3: use sort and Binary Search
        """ 
        nums = sorted(nums)
        left = 0 
        right = len(nums)
        mid = (left + right)/2
        while left < right: 
            mid = (left + right)/2
            if nums[mid] > mid:
                right = mid 
            else:
                left = mid + 1 
        return left 
        """ 