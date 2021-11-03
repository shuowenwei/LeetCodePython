# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/decode-ways/

solution: https://www.youtube.com/watch?v=qli-JCrSwuk

 and https://leetcode.com/problems/decode-ways/discuss/30352/Accpeted-Python-DP-solution

"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(s, k, memo):
            if k == 0: 
                return 1 
            l = len(s) - k 
            if s[l] == '0':
                return 0
            if memo[k] != 0:
                return memo[k]
            result = helper(s, k-1, memo)
            if k >= 2 and int(s[l:l+2]) <= 26: 
                result += helper(s, k-2, memo)
            memo[k] = result 
            return result 
        memo = [0] * (len(s) + 1 )
        return helper(s, len(s), memo)
    
        """
        if len(s) == 0: 
            return 0 
        dp = [0]*(len(s)+1) 
        dp[0] = 1 
        for i in range(1,len(s)+1): 
            if s[i-1] != '0': 
                dp[i] = dp[i] + dp[i-1]
            if i > 1 and s[i-2:i] > "09" and s[i-2:i] < "27": #"01, 02 ... , 08"ways = 0
                dp[i] = dp[i] + dp[i-2]
        return dp[len(s)]
        """
        