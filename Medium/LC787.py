# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/cheapest-flights-within-k-stops/

https://labuladong.gitee.io/algo/3/26/87/

LC931, LC64, LC174, LC514
LC787
"""
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        src2dst = {}
        for frm, to, price in flights:
            if frm in src2dst:
                src2dst[frm].append((to,price))
            else:
                src2dst[frm] = [(to,price)] 

        dp_table = {}
        def dp(src2dst, src, dst, k):
            if src == dst:
                return 0 
            if k == -1 or src not in src2dst:
                return 2**31
            if (src, dst, k) in dp_table:
                return dp_table[(src, dst, k)]
            
            res = 2**31 
            for d, price in src2dst[src]:
                res = min(res, price + dp(src2dst, d, dst, k-1))
            dp_table[(src, dst, k)] = res
            return res 
        final_res = dp(src2dst, src, dst, k)
        return -1 if final_res == 2**31 else final_res

