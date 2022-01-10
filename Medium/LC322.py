# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/coin-change/

https://labuladong.gitee.io/algo/1/3/
https://labuladong.gitee.io/algo/3/22/66/

LC509, LC322, LC518, LC416
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # solution 1: use a dictionary as a dp_table  
        # """
        dp_table = {} 
        def getMinCoins(coins, amount):
            if amount == 0: # base case
                dp_table[0] = 0
                return 0
            if amount < 0: # base case
                return 2**32
            if amount in dp_table:
                return dp_table[amount]
            res = 2**32
            for c in coins:
                res = min(res, 1 + getMinCoins(coins, amount-c))
            dp_table[amount] = res
            return res
        final_res = getMinCoins(coins, amount) 
        # return -1 if final_res == 2**32 else final_res
        return -1 if dp_table[amount] == 2**32 else dp_table[amount]
        """
        # solution 2: use an array as a dp_table  
        dp_table = [2**31-1]*(amount+1)
        dp_table[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i-c >= 0:
                    # dp_table[c] = 1 since dp_table[0] = 0
                    dp_table[i] = min(dp_table[i], dp_table[i-c] + 1)
        return -1 if dp_table[amount] == 2**31-1 else dp_table[amount]
        """
    