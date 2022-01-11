# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/super-egg-drop/

https://labuladong.gitee.io/algo/3/25/89/
https://mp.weixin.qq.com/s/xn4LjWfaKTPQeCXR0qDqZg - dp 

https://labuladong.gitee.io/algo/3/25/90/ - binary search 

LC887, LC312
"""
class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        dp_table = {}
        def dp(k, n):
            if k == 1: # 当鸡蛋数K为 1 时，显然只能线性扫描所有楼层
                return n 
            if n in (0,1): #当楼层数N等于 0 时，显然不需要扔鸡蛋
                return n 
            if (k,n) in dp_table:
                return dp_table[(k,n)]
            res = n # this is max possible
            # for i in range(1, n+1):
            #     res = min(res, 1 +               # 在第 i 楼扔了一次
            #                    max(dp(k-1, i-1), # 如果鸡蛋碎了，那么鸡蛋的个数K应该减一，搜索的楼层区间应该从[1..N]变为[1..i-1]共i-1层楼；
            #                       dp(k, n-i)))   # 如果鸡蛋没碎，那么鸡蛋的个数K不变，搜索的楼层区间应该从 [1..N]变为[i+1..N]共N-i层楼。
            low, high = 1, n
            while low <= high: 
                mid = (low + high)/2
                broken = dp(k - 1, mid - 1) # 碎
                not_broken = dp(k, n - mid) # 没碎
                if broken > not_broken: 
                    high = mid - 1 
                    res = min(res, broken + 1)
                else: 
                    low = mid + 1 
                    res = min(res, not_broken + 1)
            dp_table[(k,n)] = res
            return res
        return dp(k,n)

        # solution 2:
# 1、无论你在哪层楼扔鸡蛋，鸡蛋只可能摔碎或者没摔碎，碎了的话就测楼下，没碎的话就测楼上。
# 2、无论你上楼还是下楼，总的楼层数 = 楼上的楼层数 + 楼下的楼层数 + 1（当前这层楼）。
# 根据这个特点，可以写出下面的状态转移方程：
# dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1
# dp[k][m - 1] 就是楼上的楼层数，因为鸡蛋个数 k 不变，也就是鸡蛋没碎，扔鸡蛋次数 m 减一；
# dp[k - 1][m - 1] 就是楼下的楼层数，因为鸡蛋个数 k 减一，也就是鸡蛋碎了，同时扔鸡蛋次数 m 减一。
        # dp_table = [[0 for i in range(n+1)] for j in range(k+1)]
        # m = 0
        # while dp_table[k][m] < n: 
        #     m += 1
        #     for i in range(1, k+1): 
        #         dp_table[i][m] = dp_table[i][m-1] + dp_table[i-1][m-1] + 1 
        # return m 