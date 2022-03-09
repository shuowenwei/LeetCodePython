# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/excel-sheet-column-title/

https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation

LC168, LC171
"""
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        res = ''
        while columnNumber > 0:
            mod = (columnNumber - 1) % 26
            res = chr(ord('A') + mod) + res
            res = capitals[mod] + res
            columnNumber = (columnNumber - 1) // 26 
            # print(mod, res, columnNumber)
        return res 
    
ob = Solution()
print(ob.convertToTitle(52))