# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/min-cost-climbing-stairs/

solution link: 
 	https://leetcode.com/problems/min-cost-climbing-stairs/discuss/190960/Easy-Python-solution-and-beat-100

"""
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        """
        # dp[n]: minimum cost to climb up to n-th step
        # dp[n] = min(dp[n-1] + cost[n-1], dp[n-2] + cost[i-2])
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])    
        return dp[len(cost)] 

        """
        """
        Intuition

        There is a clear recursion available: the final cost f[i] to climb the staircase from some step i is f[i] = cost[i] + min(f[i+1], f[i+2]). This motivates dynamic programming.

        Algorithm

        Let's evaluate f backwards in order. That way, when we are deciding what f[i] will be, we've already figured out f[i+1] and f[i+2].

        We can do even better than that. At the i-th step, let f1, f2 be the old value of f[i+1], f[i+2], and update them to be the new values f[i], f[i+1]. We keep these updated as we iterate through i backwards. At the end, we want min(f1, f2).

        """
        """
        f1 = f2 = 0 
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)
        """
        length = len(cost)
        if length <= 2: 
            return min(cost)
        count1 = cost[length - 1]
        count2 = cost[length - 2]
        i = length - 3 
        while i >= 0:
            if count2 > count1:
                count1, count2 = count2, cost[i] + count1
            else: 
                count1,count2 = count2,cost[i] + count2
            i = i - 1 
        return min(count1, count2)