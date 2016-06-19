# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/rectangle-area/

"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rectangle1_area = (C-A)*(D-B)
        rectangle2_area = (G-E)*(H-F)
        intersect = 0 
        if A<G and B<H and C>E and F<D: 
            intersect = (min(C,G) - max(A,E)) * (min(D,H) - max(B,F)) 
        return rectangle1_area + rectangle2_area - intersect