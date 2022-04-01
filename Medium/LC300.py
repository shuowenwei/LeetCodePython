# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-increasing-subsequence/

https://labuladong.gitee.io/algo/3/25/77/

LC300, LC354, LC1996 -> binary search
LC509, LC322 
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
                    dp_table[i] = max(dp_table[i], dp_table[j] + 1)
        # print(dp_table)
        return max(dp_table) # not dp_table[len(nums)-1]
        
        # solution 2: 其实最长递增子序列和一种叫做 patience game 的纸牌游戏有关，甚至有一种排序方法就叫做 patience sorting（耐心排序)
        # 只能把点数小的牌压到点数比它大的牌上；
        # 如果当前牌点数较大没有可以放置的堆，则新建一个堆，把这张牌放进去；
        # 如果当前牌有多个堆可供选择，则选择最左边的那一堆放置。
        """
        piles = 0 # // 牌堆数初始化为 0
        top = [0]*len(nums) # assuming no negative number in the sequence
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
        