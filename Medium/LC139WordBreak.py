# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/word-break/

solution: https://www.youtube.com/watch?v=RPeTFTKwjps

https://leetcode.com/problems/word-break/discuss/43788/4-lines-in-Python

"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp with bottom up
        # dp[i] tells whether s[:i] can be built in wordDict 
        dp = [False] * (len(s) + 1) 
        dp[0] = True # this is empty string: ''
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True 
                    break 
        return dp[-1]
    
        """ 
        # DP with top-down and memoize 
        self.memo = {}
        def helper(ss, wordDict):
            if ss in self.memo:
                return self.memo[ss]
            if ss in wordDict:
                self.memo[ss] = True 
                return True
            for i in range(len(ss)):
                if helper(ss[:i], wordDict) is False:
                    continue 
                elif helper(ss[i:], wordDict):
                    self.memo[ss] = True 
                    return True 
            self.memo[ss] = False 
            return False
        return helper(s, wordDict)
        """