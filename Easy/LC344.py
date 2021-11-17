# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reverse-string/

labuladong: https://labuladong.gitee.io/algo/2/21/54/

"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        # You must do this by modifying the input array in-place with O(1) extra memory.
        left, right = 0, len(s)-1
        while left < right: 
            # tmp = s[left]
            # s[left] = s[right]
            # s[right] = tmp
            s[left], s[right] = s[right], s[left]
            left += 1 
            right -= 1
            