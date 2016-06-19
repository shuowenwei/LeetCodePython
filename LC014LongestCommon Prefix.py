# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-common-prefix/

"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = '' 
        if len(strs) == 0:
            return lcp
        else:
            lcp = strs[0]
        #if len(lcp) == 0:
        #    return lcp
        for e in strs: 
            new_lcp = '' 
            if len(e)==0 or len(lcp)==0:
                return ''
            for i in range(min(len(e),len(lcp)) ):
                if e[i] == lcp[i]:
                    new_lcp += e[i]
                else:
                    break 
            if len(new_lcp) == 0:
                return ''
            else:
                lcp = new_lcp
        return lcp 
