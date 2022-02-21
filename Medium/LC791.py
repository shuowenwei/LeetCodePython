# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/custom-sort-string/

"""
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        dict_order_list = collections.defaultdict(list)
        for char in order:
            dict_order_list[char] = list()
            
        for char in s:
            if char in dict_order_list:
                dict_order_list[char].append(char)
            else:
                dict_order_list[-1].append(char)
                
        res = []
        for char in order:
            res += dict_order_list[char]
        res += dict_order_list[-1]
        return ''.join(res)
                