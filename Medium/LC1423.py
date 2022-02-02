# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

"""
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        res = sum(cardPoints)
        if len(cardPoints) <= k:
            return res 
        unPickedWindow = len(cardPoints) - k
        runningSum = 0
        minWinSum = 2**32
        for i in range(len(cardPoints)):
            runningSum += cardPoints[i]
            if i + 1 >= unPickedWindow:
                minWinSum = min(minWinSum, runningSum)
                runningSum -= cardPoints[i+1-unPickedWindow]
        return res - minWinSum
    

        # my 1st solution, O(n^2) -- Time Limit Exceeded
        if len(cardPoints) <= k:
            return sum(cardPoints)
        res = 0
        for i in range(k+1):
            j = k - i
            if j > 0:
                tmp = sum(cardPoints[:i]) + sum(cardPoints[-j:])
            else: 
                tmp = sum(cardPoints[:i])
            res = max(res, tmp)
        return res

