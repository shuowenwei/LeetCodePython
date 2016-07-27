# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if profit is None:
            return 0 
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                profit = profit + prices[i+1] - prices[i]
        return profit 