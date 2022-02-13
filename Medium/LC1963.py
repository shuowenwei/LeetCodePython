# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/discuss/1390249/JavaPython-3-Space-O(1)-time-O(n)-codes-w-brief-explanation.

LC20, LC921, LC1541, LC1963, LC301
"""
class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack_open = []
        imbalanced = 0
        lst_s = list(s)
        for i in range(len(lst_s)):            
            if lst_s[i] == '[':
                stack_open.append(i)
            elif lst_s[i] == ']':
                if stack_open:
                    stack_open.pop()
                else:
                    imbalanced += 1
        return (imbalanced + 1) / 2
                
