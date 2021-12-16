# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-the-celebrity/

"""
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        cand = 0 
        for i in range(n):
            if knows(cand, i):
                # cand knows i, hence cand is not celebrity, just not sure about i 
                cand = i 
            else:
                # just not sure about i 
                pass 
            
        # now check cand 
        for i in range(n):
            if i == cand:
                continue
            if not knows(cand, i) and knows(i, cand):  # cand must know nobody, at the meantime everyone should know cand 
                return -1 
        return cand 
            