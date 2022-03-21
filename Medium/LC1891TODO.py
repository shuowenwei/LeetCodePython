# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/cutting-ribbons/

https://walkccc.me/LeetCode/problems/1891/

LC875, LC1011, lC1891

go read https://www.geeksforgeeks.org/maximum-length-possible-by-cutting-n-given-woods-into-at-least-k-pieces/
"""
class Solution(object):
    def maxLength(self, ribbons, k):
        def getNumCut(max_ribbon_length):
            count = 0
            for ribbon in ribbons:
                count += ribbon // max_ribbon_length
            return count

        left = 1
        right = sum(ribbons) // k + 1
        while left <= right:
            mid = left + (right - left) // 2
            count = getNumCut(mid)
            if count < k: # max_ribbon_length must be shorter
                right = mid - 1
            elif count > k: # max_ribbon_length could be longer 
                left = mid + 1 
            elif count == k: # max_ribbon_length could be longer 
                # // 搜索右侧边界，则需要收缩左侧边界
                left = mid + 1
        return right # or left - 1 # not left, this is right_boundry search 

"""
    def maxLength2(self, ribbons, k):
        def isCutPossible(length):
            count = 0
            for ribbon in ribbons:
                count += ribbon // length
            return count >= k
        l = 1
        r = sum(ribbons) // k + 1
        while l < r:
            m = (l + r) // 2
            if not isCutPossible(m):
                r = m
            else:
                l = m + 1
        return l - 1
    
sol = Solution()

ribbons = [9,7,5]
k = 3
expected = 5
print(sol.maxLength(ribbons, k), expected, sol.maxLength2(ribbons, k))

ribbons = [7,5,9]
k = 4
expected = 4 
print(sol.maxLength(ribbons, k), expected, sol.maxLength2(ribbons, k))

ribbons = [5,7,9]
k = 22
expected = 0
print(sol.maxLength(ribbons, k), expected, sol.maxLength2(ribbons, k))
"""