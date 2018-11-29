# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/guess-number-higher-or-lower/

"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1 
        right = n
        if guess(left) == 0:
            return left
        if guess(right) == 0:
            return right 
        mid = (left + right)/2
        while guess(mid) != 0: 
            if guess(mid) == -1:
                right = mid 
                mid = (left + right)/2
            else:
                left = mid 
                mid = (left + right)/2
        return mid 

        """
        left = 1 
        right = n
        if guess(left) == 0:
            return left
        if guess(right) == 0:
            return right 
        mid = (left + right)/2
        while left <= right:
            mid = left + (right - left)/2
            temp = guess(mid)
            if temp == 0:
                return mid 
            if temp == -1:
                right = mid 
                mid = (left + right)/2
            if temp == 1:
                left = mid 
                mid = (left + right)/2
        return mid 
        """