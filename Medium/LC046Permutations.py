# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/permutations/

solution reference link: https://discuss.leetcode.com/topic/6377/my-ac-simple-iterative-java-python-solution/2

"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]] 
        for n in nums: 
            new_perms = [] 
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perms.append( perm[:i]+[n]+perm[i:] )
            perms = new_perms
        return perms 