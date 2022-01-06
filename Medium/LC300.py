# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-increasing-subsequence/

https://labuladong.gitee.io/algo/3/23/67/

LC509, LC322
LC300, LC354 -> binary search
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_table = [1]*(len(nums))
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_table[i] = max(dp_table[i], dp_table[j]+1)
        # print(dp_table)
        return max(dp_table) # not dp_table[len(nums)-1]
        
        # solution 2: 其实最长递增子序列和一种叫做 patience game 的纸牌游戏有关，甚至有一种排序方法就叫做 patience sorting（耐心排序
        """
        piles = 0 # // 牌堆数初始化为 0
        top = [0]*len(nums)
        for i in range(len(nums)):
            poker = nums[i] # // 要处理的扑克牌
            # /***** 搜索左侧边界的二分查找 *****/
            left, right = 0, piles
            while left < right:
                mid = (right + left)/2
                if top[mid] > poker:
                    right = mid 
                elif top[mid] < poker:
                    left = mid + 1 
                else:
                    right = mid 
            # /*********************************/
            # // 没找到合适的牌堆，新建一堆
            if left == piles:
                piles += 1 
            # // 把这张牌放到牌堆顶
            top[left] = poker 
        return piles
        """