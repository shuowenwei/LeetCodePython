# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/count-numbers-with-unique-digits/

solution reference link: 
https://discuss.leetcode.com/topic/48332/java-o-1-with-explanation

"""
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
This is a digit combination problem. Can be solved in at most 10 loops.

When n == 0, return 1. I got this answer from the test case.

When n == 1, _ can put 10 digit in the only position. [0, ... , 10]. Answer is 10.

When n == 2, _ _ first digit has 9 choices [1, ..., 9], second one has 9 choices excluding the already chosen one. So totally 9 * 9 = 81. answer should be 10 + 81 = 91

When n == 3, _ _ _ total choice is 9 * 9 * 8 = 684. answer is 10 + 81 + 648 = 739

When n == 4, _ _ _ _ total choice is 9 * 9 * 8 * 7.

...

When n == 10, _ _ _ _ _ _ _ _ _ _ total choice is 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

When n == 11, _ _ _ _ _ _ _ _ _ _ _ total choice is 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 * 0 = 0
        """
        if n > 10:
            return 0
        if n == 0:
            return 1
            
        res = 10 
        base = 9 
        for i in range(2, n+1): 
            base = base*( 10 - i + 1)
            res = res + base 
        return res 
        
