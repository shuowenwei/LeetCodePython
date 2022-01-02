# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/freedom-trail/

https://labuladong.gitee.io/algo/3/26/86/

LC931, LC64, LC174, LC514
"""
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        def getIndices(ring, letter):
            res = []
            for i, l in enumerate(ring):
                if letter == l:
                    res.append(i)
            return res
        
        dp_table = {}
        def dp(ring, key, ringP, keyP):
            if keyP == len(key):
                return 0
            if (ringP, keyP) in dp_table:
                return dp_table[(ringP, keyP)]

            res = 2**31-1 
            choices = getIndices(ring, key[keyP])
            for c in choices:
                moves = abs(ringP - c)
                moves = min(moves, len(ring)-moves)
                res = min(res, moves+dp(ring, key, c, keyP+1))
            dp_table[(ringP, keyP)] = res
            return res
        return dp(ring, key, 0, 0) + len(key)

