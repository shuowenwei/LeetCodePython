# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/coin-change/

labuladong: https://labuladong.gitee.io/algo/1/3/

"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0 
        dp_table = {0:0}
        
        def getMinCoins(coins, amount):
            if amount < 0:
                return -1 
            if amount in dp_table:
                return dp_table[amount]
            res = 2**32
            for c in coins:
                tmp_res = getMinCoins(coins, amount-c)
                if tmp_res == -1:
                    continue
                res = min(res, 1 + tmp_res)
            if res ==  2**32:
                dp_table[amount] = -1 
            else:
                dp_table[amount] = res 
            return res
        
        final_res = getMinCoins(coins, amount)
        return dp_table[amount]
