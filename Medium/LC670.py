# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-swap/

refer to https://leetcode.com/problems/maximum-swap/discuss/185982/Straightforward-O(n)-python
"""
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        list_num = [int(n) for n in str(num)]
        res = num 
        cur_max_id = len(list_num) - 1
        for i in range(len(list_num) - 1, -1, -1):
            if list_num[i] > list_num[cur_max_id]:
                cur_max_id = i 
            elif list_num[cur_max_id] > list_num[i] and i != cur_max_id:
                # swap to get on candidate
                list_num[cur_max_id], list_num[i] = list_num[i], list_num[cur_max_id]
                res = max(res, int(''.join([str(s) for s in list_num])))
                # swap back, max possible candidate is saved in res
                list_num[cur_max_id], list_num[i] = list_num[i], list_num[cur_max_id]                
        return res 

