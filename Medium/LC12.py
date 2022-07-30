# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/integer-to-roman/

https://leetcode.com/problems/integer-to-roman/discuss/6304/Python-simple-solution.

LC12, LC13
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # solution 1 and 2
        # https://leetcode.com/problems/integer-to-roman/discuss/6304/Python-simple-solution.
        integers = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        romans = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        # dctInteger2Roman = {n:r for n,r in zip(integers, romans)}
        res = ''
        i = 0
        while num:
            res = res + (num//integers[i]) * romans[i]
            num = num % integers[i]
            i += 1
        return res 

        # solution 2:
        integers = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        romans = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for i, v in enumerate(integers):
            res += (num//v) * romans[i]
            num %= v
        return res


        # solution 3: 
        # https://www.youtube.com/watch?v=VHcO328FY6M
        integers = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        romans = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ''
        for i in range(len(integers)):
            while num >= integers[i]:
                num = num - integers[i]
                res += romans[i]
        return res 