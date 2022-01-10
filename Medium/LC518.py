# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/coin-change-2/

https://labuladong.gitee.io/algo/3/24/82/

LC509, LC322, LC518, LC416
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
        """
        # solution 2:
        # dp[i][j] 的定义如下：
        # 若只使用前 i 个物品（可以重复使用），当背包容量为 j 时，有 dp[i][j] 种方法可以装满背包。
        # 换句话说，翻译回我们题目的意思就是：
        # 若只使用 coins 中的前 i 个硬币的面值，若想凑出金额 j，有 dp[i][j] 种凑法。
        dp_table = [ [0] * (amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp_table[i][0] = 1
        # note: these two for loops are exchangeable!!!!!!
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j - coins[i-1] >= 0:
                    # 首先由于 i 是从 1 开始的，所以 coins 的索引是 i-1 时表示第 i 个硬币的面值。
                    # 若只使用前 i 个物品（可以重复使用），当背包容量为 j-coins[i-1] 时，有 dp[i][j-coins[i-1]] 种方法可以装满背包。
                    dp_table[i][j] = dp_table[i-1][j] + dp_table[i][j-coins[i-1]]
                else: 
                    dp_table[i][j] = dp_table[i-1][j]
        # print(dp_table)
        return dp_table[len(coins)][amount]
        """