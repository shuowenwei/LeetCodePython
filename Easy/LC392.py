# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/is-subsequence/submissions/

https://labuladong.gitee.io/algo/4/32/141/

LC392
- BinarySearch
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # my solution: two pointers
        ps, pt = 0, 0
        while ps < len(s) and pt < len(t):
            if t[pt] == s[ps]:
                ps += 1
                pt += 1
            else:
                pt += 1
        return ps == len(s)        
                
        # solution 2: 
        # 二分查找返回目标值 val 的索引，对于搜索左侧边界的二分查找，有一个特殊性质：
        # 当 val 不存在时，得到的索引恰好是比 val 大的最小元素索引。
        def left_bound(nums, target):
            left = 0
            right = len(nums) - 1 
            while left <= right: # break when left == right + 1 
                mid = (left + right) / 2 
                if nums[mid] == target:
                    right = mid - 1 
                elif nums[mid] < target:
                    left = mid + 1 
                elif nums[mid] > target:
                    right = mid - 1
            if left > len(nums) - 1  or nums[left] != target: 
                return -1 
            return left
        
        dict_t = {}
        for i, char in enumerate(t):
            if char not in dict_t:
                dict_t[char] = [i]
            else:
                dict_t[char].append(i)
        j = 0 # 串 t 上的指针
        for i in range(len(s)):
            if s[i] not in dict_t:
                return False
            pos = left_bound(dict_t[s[i]], j)
            if pos == len(dict_t[s[i]]):
                return False 
            j = dict_t[s[i]][pos] + 1
        return True