# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-palindrome/

"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
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