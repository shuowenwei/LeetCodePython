# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/count-and-say/

"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def generateNext(s):
            current = 0
            next = 1
            length = len(s) 
            s = s + '#'
            count_say = ''
            while current < length and next < length + 1: 
                if s[current] != s[next]:
                    count_say = count_say + str(next-current) + s[current]
                    current = next
                    next += 1
                else: 
                    next += 1
            return count_say
            
        s = '1'
        for _ in range(1,n):
            s = generateNext(s)
        return s 