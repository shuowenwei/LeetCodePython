# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/combinations/
https://mp.weixin.qq.com/s/qT6WgR6Qwn7ayZkI3AineA

LC698, LC78, LC46, LC77, LC22, LC659
LC51, LC37
- backtracking
LC78, LC77, LC90
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # refer to LC78
        res = []
        def backtracking(n, k, start, tmp):
            # // 前序位置，每个节点的值都是一个子集
            if len(tmp) == k:
                res.append(tmp[::]) # // 遍历到了第 k 层，收集当前节点的值
                return 
            for i in range(start, n+1):
                tmp.append(i)
                #  // 通过 start 参数控制树枝的遍历，避免产生重复的子集
                backtracking(n, k, i+1, tmp)
                tmp.pop()
        backtracking(n, k, 1, [])
        return res 
        