# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/candy/


solution: https://leetcode.com/problems/candy/solution/

"""
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        left = [1] * len(ratings)
        right = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]: 
                left[i] = left[i-1] + 1 
            
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                right[j] = right[j+1] + 1
        res = 0 
        for l, r in zip(left, right):
            res += max(l,r)
        return res