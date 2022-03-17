# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/split-array-into-consecutive-subsequences/

LC659, LC1296
"""
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = collections.defaultdict(int)
        need = collections.defaultdict(int)
        for n in nums:
            # if n not in freq:
            #     freq[n] = 0
            # if n+1 not in freq:
            #     freq[n+1] = 0
            # if n+2 not in freq:
            #     freq[n+2] = 0
            freq[n] += 1
            
        for v in nums:
            if freq[v] == 0:
                # // 已经被用到其他子序列中
                continue
            
            # // 先判断 v 是否能接到其他子序列后面
            if v in need and need[v] > 0:
                # // v 可以接到之前的某个序列后面
                freq[v] -= 1
                # // 对 v 的需求减一
                need[v] -= 1
                # // 对 v + 1 的需求加一
                need[v+1] += 1
                # if v+1 in need:
                #     need[v+1] += 1
                # else:
                #     need[v+1] = 1
            elif freq[v] > 0 and freq[v+1] > 0 and freq[v+2] > 0:
                # // 将 v 作为开头，新建一个长度为 3 的子序列 [v,v+1,v+2]
                freq[v] -= 1
                freq[v+1] -= 1
                freq[v+2] -= 1
                # // 对 v + 3 的需求加一
                need[v+3] += 1
                # if v+3 in need:
                #     need[v+3] += 1
                # else:
                #     need[v+3] = 1
            else:
                # // 两种情况都不符合，则无法分配
                return False
            
        return True
