# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/integer-break/

not sure this is a good solution 

"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #if n == 2: 
        #    return 1 
        
        # 1 return 0, 2 return 1
        res = [0,1,2,4,6,9]     
        if n < 7:
            return res[n-1]

        for i in range(7,n+1):
            newNum = max(res[-2]*2, res[-3]*3 )
            res.append(newNum)
        return res[-1]