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
        """ solution 1: use a dictionary as a dp_table  
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
        
        _ = getMinCoins(coins, amount)
        return dp_table[amount]
        """
        # solution 2: use an array as a dp_table  
        dp_table = [amount+1]*(amount+1)
        dp_table[0] = 0 
        for i in range(amount+1):
            for c in coins:
                if amount - c < 0:
                    continue
                else:
                    dp_table[i] = min(dp_table[i], dp_table[i-c] + 1)
        if dp_table[amount] == amount+1:
            return -1 
        else:
            return dp_table[amount]

