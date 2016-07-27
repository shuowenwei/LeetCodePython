# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

solution link: 
 	https://leetcode.com/discuss/97355/share-my-simple-python-code-using-method-with-explaination

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
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
