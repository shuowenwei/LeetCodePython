# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/coin-change-2/

https://labuladong.gitee.io/algo/3/24/82/

LC509, LC322, LC518
"""
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp_table = [0] * (amount+1)
        dp_table[0] = 1
        coins.sort()
        for c in coins:
            for i in range(amount+1):
                if i >= c:
                    dp_table[i] = dp_table[i] + dp_table[i-c]
                # else: # c - i > 0
                #     continue 
        # print(dp_table)
        return dp_table[amount]