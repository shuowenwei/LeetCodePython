# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/super-egg-drop/

https://labuladong.gitee.io/algo/3/26/89/
https://mp.weixin.qq.com/s/xn4LjWfaKTPQeCXR0qDqZg - dp 

https://labuladong.gitee.io/algo/3/26/90/ - binary search 

LC887
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
            #     # 如果鸡蛋碎了，那么鸡蛋的个数K应该减一，搜索的楼层区间应该从[1..N]变为[1..i-1]共i-1层楼；
            #     res = min(res, max(dp(k-1, i-1), 
            #     # 如果鸡蛋没碎，那么鸡蛋的个数K不变，搜索的楼层区间应该从 [1..N]变为[i+1..N]共N-i层楼。
            #                        dp(k, n-i)
            #                       ) + 1) # 在第 i 楼扔了一次
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
