# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/stone-game/

https://labuladong.gitee.io/algo/3/25/92/

"""
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        # dp[i][j].fir = x 表示，对于 piles[i...j] 这部分石头堆，先手能获得的最高分数为 x。# [0]
        # dp[i][j].sec = y 表示，对于 piles[i...j] 这部分石头堆，后手能获得的最高分数为 y。# [1]
        dp_table = [ [[0, 0] for i in range(n)] for j in range(n)]
        #base case
        for i in range(n):
            dp_table[i][i][0] = piles[i]
            dp_table[i][i][0] = 0
            
        for i in range(n-2, -1, -1):
            for j in range(i, n):
                # // 先手选择最左边或最右边的分数
                left = piles[i] + dp_table[i+1][j][1]
                right = piles[j] + dp_table[i][j-1][1]
                if left > right:
                    dp_table[i][j][0] = left
                    dp_table[i][j][1] = dp_table[i+1][j][1]
                else:
                    dp_table[i][j][0] = right
                    dp_table[i][j][1] = dp_table[i][j-1][0]
        # print(dp_table)     
        return dp_table[0][n-1][0] - dp_table[0][n-1][1]
