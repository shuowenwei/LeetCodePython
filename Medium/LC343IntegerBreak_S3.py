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
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        res = 3**(n/3)
        if n%3 == 1:
            return res*4/3  
        elif n%3 == 2: 
            return res*2
        else:
            return res 
        """
        list_3 = [3] * (n/3) # generate a list of 3
        mod_3 = n%3
        if mod_3 == 1: # if a 1 is left, then add it to the first element to get a 4
            list_3[0] += 1
        if mod_3 == 2: # if a 2 is left, then put it into the list
            list_3.append(2)
        return reduce(lambda a, b: a*b, list_3)
        """

        """
The key for this problem is that we need to break the number to 2s, 3s and 4s.
First we need to know a fact that,if a,b > 3, |a-b| <= 1, then a*b>=a+b.

So, if n = a + b, a = a1+a2, b=b1+b2, we should break n to a1+a2+b1+b2, |a1-a2|<1 and |b1-b2|<1 instead of a + b, because a1*a2>a, b1*b2>b. However, we shall stop when we get a 3 or 2, so what we shall do is to find the list of 3 and 2.

You may have noticed why the 4 appeared. 'Cause if we break 4, we get 2+2, and 2+2 = 2*2, so it's the same with the condition that we get two 2.

        """