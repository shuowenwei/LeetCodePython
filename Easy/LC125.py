# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-palindrome/

LC680, LC125
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        s = s.lower()
        alphanumeric = set(list('0123456789abcdefghijklmnopqrstuvwxyz'))
        while left < right:
            if s[left] not in alphanumeric: 
                left += 1
            elif s[right] not in alphanumeric: 
                right -= 1
            elif s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True 
    
        # using regular expression is also fine 
        import re 
        s_nopun = re.sub(r'\W+','',s).lower() 
        if len(s_nopun) == 0:
            return True
        left = 0
        right = len(s_nopun) - 1 
        while(left < right):
            if s_nopun[left] == s_nopun[right]:
                left += 1
                right -= 1
            else:
                return False 
        return True