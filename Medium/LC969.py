# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/pancake-sorting/

https://labuladong.gitee.io/algo/4/32/134/

"""
class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        res = []
        def reverse(arr, i, j):
            while i < j:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                i += 1
                j -= 1
        def flip(arr):
            n = len(arr)
            if n == 1:
                return
            max_val = max(arr)
            for i, a in enumerate(arr):
                if a == max_val:
                    if i == n-1:
                        break
                    else:
                        reverse(arr, 0, i)
                        res.append(i+1)
                        reverse(arr, 0, n-1)
                        res.append(n)
                        break
            flip(arr[:n-1])

        flip(arr)
        return res 
            
