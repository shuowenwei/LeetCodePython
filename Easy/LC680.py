# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-palindrome-ii/

LC680, LC125
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True 

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] == s[right-1] or s[left+1] == s[right]:
                s1 = s[left: right]
                s2 = s[left+1: right+1]
                return isPalindrome(s1) or isPalindrome(s2)
            else:
                return False
        return True 