# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/interval-list-intersections/

https://labuladong.gitee.io/algo/4/32/138/
https://mp.weixin.qq.com/s/Eb6ewVajH56cUlY9LetRJw

LC1288, LC56, LC986
"""
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        p1, p2 = 0, 0
        while p1 < len(firstList) and p2 < len(secondList):
            firstLeft, firstRight = firstList[p1]
            secondLeft, secondRight = secondList[p2]
            if firstRight < secondLeft:
                p1 += 1
            elif firstLeft > secondRight:
                p2 += 1
            else:
                left = max(firstLeft, secondLeft)
                if firstRight > secondRight:
                    res.append([left, secondRight])
                    p2 += 1
                elif firstRight < secondRight:
                    res.append([left, firstRight])
                    p1 += 1
                else: # == 
                    res.append([left, firstRight]) # res.append([left, secondRight])
                    p1 += 1 
                    p2 += 1
        return res 