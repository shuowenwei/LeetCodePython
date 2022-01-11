# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

https://labuladong.gitee.io/algo/1/11/

LC121, LC122, LC123, LC188, LC309, LC714
"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        import numpy as np 
        n = len(prices)
        if n <= 0:
            return 0
        if k > n/2: # same as k = +infinity, hence k and k-1 are the same 
            dp = np.zeros((n,2)) # 0: no stock, 1: have stock
            for i in range(n):
                if i-1 == -1:
                    dp[i][0] = 0
                    # dp[i][0] = max(dp[-1][0], dp[-1][1] + prices[i])
                    #          = max(0, -infinity + prices[i]) = 0 
                    dp[i][1] = -prices[i]
                    # dp[i][1] = max(dp[-1][1], dp[-1][0] - prices[i])
                    #          = max(-infinity, 0 - prices[i]) =  -prices[i]
                    continue 
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            return int(dp[n-1][0]) # at (n-1)th day, no stock left

        max_k = k
        # dp[i][k][0 or 1]
        # 0 <= i <= n - 1, 1 <= k <= K
        dp = np.zeros((n, max_k+1, 2)) # 0: no stock, 1: have stock
        for i in range(n):
            for k in range(max_k, 0, -1):
                if i-1 == -1:
                    dp[i][k][0] = 0
                    # dp[i][0] = max(dp[-1][0], dp[-1][1] + prices[i])
                    #          = max(0, -infinity + prices[i]) = 0 
                    dp[i][k][1] = -prices[i]
                    # dp[i][1] = max(dp[-1][1], dp[-1][0] - prices[i])
                    #          = max(-infinity, 0 - prices[i]) =  -prices[i]
                    continue 
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return int(dp[n-1][max_k][0]) # at (n-1)th day, no stock left
