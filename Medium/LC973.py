# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/k-closest-points-to-origin/

LC215, LC973, LC658, LC347, LC692
"""
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        import random
        lst_dist = [(x**2 + y**2, x, y) for x, y in points]
        self.res = []
        def helper(lst_dist, k):
            if k <= 0:
                return
            random.shuffle(lst_dist)
            pivot = lst_dist[0]
            small = [e for e in lst_dist if e[0] < pivot[0] ]
            equal = [e for e in lst_dist if e[0] == pivot[0] ]
            large = [e for e in lst_dist if e[0] > pivot[0] ]
            if k <= len(small):
                helper(small, k)
            # elif k - len(small) <= len(equal): # The answer is guaranteed to be unique
            #     for d,x,y in small+equal: # must have equal
            #         self.res.append([x,y])
            #     helper(equal, k - len(small) - len(equal))
            else:
                for d,x,y in small+equal:
                    self.res.append([x,y])
                helper(large, k - len(small) - len(equal) )

        helper(lst_dist, k)
        return self.res 

        # solution 2, user a minheap via heapq, O(nlog(n))
        from heapq import heappop, heappush, heapify
        lst_dist = [(x**2 + y**2, x, y) for x, y in points]
        heapify(lst_dist)
        res = []
        for i in range(k):
            distance, i, j = heappop(lst_dist)
            res.append([i,j])
        return res

