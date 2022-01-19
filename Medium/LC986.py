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
            if firstList[p1][1] < secondList[p2][0]:
                p1 += 1
            elif firstList[p1][0] > secondList[p2][1]:
                p2 += 1
            else:
                left = max(firstList[p1][0], secondList[p2][0])
                if firstList[p1][1] > secondList[p2][1]:
                    res.append([left, secondList[p2][1]])
                    p2 += 1
                elif firstList[p1][1] < secondList[p2][1]:
                    res.append([left, firstList[p1][1]])
                    p1 += 1
                else: # == 
                    res.append([left, firstList[p1][1]])
                    p1 += 1 
                    p2 += 1
        return res 
