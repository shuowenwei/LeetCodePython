# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/permutation-in-string/

labuladong: https://labuladong.gitee.io/algo/1/9/

lC76, LC567, LC438, LC3

"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        t = s1 
        s = s2
        if len(s) < len(t):
            return ''
        
        need = {char: t.count(char) for char in t}
        window = {char: 0 for char in t}
        left, right = 0, 0 
        valid = 0
        while right < len(s): 
            c = s[right]
            right += 1 
            if need.get(c) is not None:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            else:
                left = right 
                window = {char: 0 for char in t}
                valid = 0
            # the substring of s2 should only contains 
            # the permutations of s1, not any other chars
            while right - left >= len(t):
                if valid == len(need):
                    return True 
                d = s[left]
                left += 1
                if need.get(d) is not None:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False

