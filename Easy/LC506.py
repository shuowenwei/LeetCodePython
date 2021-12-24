# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/relative-ranks/

"""
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        rank = [(index, s) for index, s in enumerate(score)]
        rank.sort(key =lambda x: x[1], reverse=True)
        res = ['']*len(score)
        for i, index_score in enumerate(rank):
            if i == 0: 
                res[index_score[0]] = 'Gold Medal'
            elif i == 1:
                res[index_score[0]] = 'Silver Medal'
            elif i == 2:
                res[index_score[0]] = 'Bronze Medal' 
            else: 
                res[index_score[0]] = str(i+1)
        return res 
