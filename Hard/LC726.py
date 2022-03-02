# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen
https://leetcode.com/problems/number-of-atoms/

https://leetcode.com/problems/number-of-atoms/discuss/140802/Python-20-lines-very-readable-simplest-and-shortest-solution-36-ms-beats-100

LC726, LC394
"""
import collections
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        dictAtom2num = collections.defaultdict(lambda:0)
        atom = ''
        num, power = 0, 0 
        coef = 1
        stack = []
        for char in formula[::-1]:
            if char.isdigit():
                num = num + int(char) * 10**power
                power += 1
            elif char == ')': # "(H)"
                stack.append(max(num, 1))
                coef = coef * max(num, 1)
                num, power = 0, 0
            elif char == '(':
                print(stack, coef)
                coef = coef // stack.pop() # "(H)" --> 0//0
                num, power = 0, 0
            elif char.isupper():
                atom += char
                dictAtom2num[atom[::-1]] += max(num, 1) * coef
                atom = ''
                num, power = 0, 0
            elif char.islower():
                atom += char
        return ''.join(k+str(v if v > 1 else '') for k,v in sorted(dictAtom2num.items()))

