# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

labuladong: https://labuladong.gitee.io/algo/1/11/

solution link: 
 	https://leetcode.com/discuss/97355/share-my-simple-python-code-using-method-with-explaination

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import numpy as np 
        n = len(prices)
        # k = 1, dp[i-1][0][0] is always 0
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
            dp[i][1] = max(dp[i-1][1], 0 - prices[i]) # dp[i-1][0][0] is always 0
        return int(dp[n-1][0]) # at (n-1)th day, no stock left 
        
        """
        if len(prices) < 2:
            return 0 
        
        profit = [prices[i] - prices[i-1] for i in range(1,len(prices))]
        runningSum = 0 
        maxAll = 0 
        for p in profit:
            runningSum = max(p, p + runningSum)
            maxAll = max(runningSum, maxAll)
        return maxAll
        """

        """
        if len(prices) < 2:
             return 0 
             
        max_last = 0 
        max_all  = 0 
        i = 1 
        while i < len(prices):
            last_profit = prices[i] - prices[i-1]
            max_last = max(last_profit, last_profit + max_last)
            max_all = max(max_all, max_last) 
            i += 1
        if max_all < 0:
            max_all = 0
        return max_all

        """

