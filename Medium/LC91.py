# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/decode-ways/

solution: https://www.youtube.com/watch?v=qli-JCrSwuk

"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: 
            return 0 
        if s[0] == '0':
            return 0
        dp_table = {}
        def dp(s, index):
            if index == 0:
                return 1
            if index in dp_table:
                return dp_table[index]
            res = 0 
            if s[index - 1] != '0':
                res = res + dp(s, index - 1)
            if index > 1 and 9 < int(s[index-2:index]) < 27:
                res = res + dp(s, index - 2)
            dp_table[index] = res
            return res
        return dp(s, len(s))
    
        """
        if len(s) == 0: 
            return 0 
        if s[0] == '0': # '06' ways = 0
            return 0
        dp = [0]*(len(s)+1) 
        dp[0] = 1 
        for i in range(1,len(s)+1): 
            if s[i-1] != '0': 
                dp[i] = dp[i] + dp[i-1]
            if i > 1 and 9 < int(s[i-2:i]) < 27: #"01, 02 ... , 08"ways = 0
                dp[i] = dp[i] + dp[i-2]
        return dp[len(s)]
        """
