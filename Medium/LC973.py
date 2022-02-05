# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/k-closest-points-to-origin/

LC215, LC973, LC658, LC347
"""
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        import random 
        distance = [(x**2+y**2, x, y) for x,y in points]
        
        def helper(distance, k, res):
            if k <= 0:
                return res
            random.shuffle(distance)
            pivot = distance[0][0]
            left = [d for d in distance if d[0] < pivot]
            equals = [d for d in distance if d[0] == pivot]
            # assert len(equals) == 1, 'Error! Answers might not be unique'
            right = [d for d in distance if d[0] > pivot]
            if k <= len(left):
                return helper(left, k, res)
            elif k - len(left) <= len(equals):
                for d, x, y in left + equals:
                    res.append([x, y])
                return helper(equals, k - len(left+equals), res)
            else:
                for d, x, y in left + equals:
                    res.append([x, y])
                return helper(right, k - len(equals+left), res)
            # return res

        res = helper(distance, k, [])
        return res 
