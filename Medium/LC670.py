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
        list_num = [int(e) for e in str(num)]
        n = len(list_num)
        res = num 
        cur_max_id = n - 1
        for i in range(n - 1, -1, -1):
            if list_num[i] > list_num[cur_max_id]:
                cur_max_id = i 
            # elif list_num[cur_max_id] > list_num[i] and i != cur_max_id:
            else:
                # swap to get one candidate
                list_num[cur_max_id], list_num[i] = list_num[i], list_num[cur_max_id]
                res = max(res, int(''.join([str(s) for s in list_num]))) # due to this, this is O(n^2)
                # swap back, max possible candidate is saved in res
                list_num[cur_max_id], list_num[i] = list_num[i], list_num[cur_max_id]                
        return res 


        # solution 2: O(n)
        """ 
        if num < 10:
            return num
        list_num = [int(e) for e in str(num)]
        res = num 
        n = len(list_num)
        post_max = [list_num[-1]] * n
        for i in range(n-2, -1, -1):
            post_max[i] = max(post_max[i+1], list_num[i])
        
        # print(post_max)
        for i, (original, post_max) in enumerate(zip(list_num, post_max)):
            # print(i, original, post_max)
            if original < post_max:
                list_num[i] = post_max
                findOrg = original
                findPost_max = post_max
                # print(list_num, findOrg, findPost_max)
                break 
            elif i == n-1:
                return int(''.join([str(s) for s in list_num]))
            
        for i in range(n-1, -1, -1):
            if list_num[i] == findPost_max:
                list_num[i] = findOrg
                break
        return int(''.join([str(s) for s in list_num]))
        """