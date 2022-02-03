# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-and-replace-in-string/submissions/

https://leetcode.com/problems/find-and-replace-in-string/discuss/130587/C%2B%2BJavaPython-Replace-S-from-right-to-left

"""
class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        
        doSthTuple = []
        for ind, src, tgt in zip(indices, sources, targets):
            src_len = len(src)
            if s[ind : ind + src_len] == src:
                doSthTuple.append( (ind, src, tgt) )
                
        new_s = ''
        doSthTuple.sort(key=lambda x: x[0], reverse=True) # replace from right to left 
        print(doSthTuple)
        for i in range(len(doSthTuple)):
            ind, src, tgt = doSthTuple[i]
            # print(ind, src, tgt)
            src_len = len(src)
            s = s[:ind] + tgt + s[ind+src_len:] 
        return s
    
