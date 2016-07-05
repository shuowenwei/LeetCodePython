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
        
        #alphanumeric = 'abcdefg...'
        #ss = "".join(for e in s if e in )
        
        middle = len(s_nopun)/2
        if len(s_nopun) == 1:
            return True 
        for i in range(middle):
            if s_nopun[i] != s_nopun[len(s_nopun)-i-1]:
                return False 
        return True 