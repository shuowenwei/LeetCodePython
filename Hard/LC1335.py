# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/490316/JavaC%2B%2BPython3-DP-O(nd)-Solution
"""
class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        if len(jobDifficulty) < d:
            return -1 
        # Use dp[i][j] where DP states are 
        # i the index of the last cut and 
        # j the number of remaining cuts. Complexity is O(n * n * d).
        dp_table = {}
        def dp(jobDifficulty, lastCut, remaingDays):
            n = len(jobDifficulty)
            if remaingDays == 1:
                res = max(jobDifficulty[lastCut:])
                dp_table[(lastCut, remaingDays)] = res
                return res 
            if (lastCut, remaingDays) in dp_table: 
                return dp_table[(lastCut, remaingDays)]
            res = 2**32
            maxDiff = 0 
            for i in range(lastCut, n - remaingDays + 1):
                maxDiff = max(maxDiff, jobDifficulty[i])
                res = min(res, dp(jobDifficulty, i + 1, remaingDays-1) + maxDiff)
            dp_table[(lastCut, remaingDays)] = res 
            return res
        res = dp(jobDifficulty, 0, d)
        # print(dp_table)
        return res 
