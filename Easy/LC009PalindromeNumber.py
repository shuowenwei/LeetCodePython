# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

LC009PalindromeNumber

https://leetcode.com/problems/palindrome-number/

"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0 or ( x > 0 and x%10==0)):
            return False 
            
        s = str(x) 
        n = len(s) 
        #if n == 2:
        #    return s[0]==s[1]

        for i in range(n/2):
            if s[i] != s[n-i-1]:
                return False

        return True  


