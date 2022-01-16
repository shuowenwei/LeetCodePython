# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximize-distance-to-closest-person/

"""
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # solution 1, too long too ugly 
        n = len(seats)
        max_distance = 1
        leftEnd = 0
        rightEnd = n-1
        for i in range(n):
            if seats[i] == 1:
                if i != 0:
                    max_distance = max(max_distance, abs(i-leftEnd))
                    leftEnd = i
        for j in range(n-1, -1, -1):
            if seats[j] == 1:
                if j != n-1:
                    max_distance = max(max_distance, abs(j-rightEnd))
                    rightEnd = j
        firstOne = 0
        lastOne = 0 
        if seats[0] == 0:
            for i in range(n):
                if seats[i] == 1:
                    firstOne = i
                    break
        if seats[n-1] == 0:
            for i in range(n-1, -1, -1):
                if seats[i] == 1:
                    lastOne = n-1-i
                    break
        return max(firstOne, max_distance/2, lastOne)
    
        # my solution: Time Limit Exceeded ... O(n^2) 77/81
        n = len(seats)
        res = [0 if s == 1 else n for s in seats]
        for i in range(n):
            for j in range(n):
                if seats[i] == 1:
                    res[j] = min(res[j], abs(i-j))
        return max(res)

        