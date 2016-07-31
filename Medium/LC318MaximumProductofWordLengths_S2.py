# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-product-of-word-lengths/

solution references: https://discuss.leetcode.com/topic/32692/a-two-line-python-solution-176-ms/4

"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        """
        d = {} 
        for w in words: 
            key = sum(1<<(ord(c) - ord('a')) for c in set(w))
            if key not in d:
                d[key] =len(w) 
            else:
                d[key] = max(d[key],len(w))
                
        res = 0
        for k1,v1 in d.items():
            for k2,v2 in d.items():
                if k1&k2 == 0:
                    res = max(res,v1*v2)
        return res 
        """

        d = dict(sorted((sum(1 << (ord(c) - 97) for c in set(w)), len(w)) for w in words))
        return max([d[k] * d[K] for k in d for K in d if not k & K] or [0])
        
        """
        maxLength = 0 
        if len(words) <= 0:
            return maxLength
            
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                a = words[i]
                b = words[j]
                if self.NoCommonChar(a,b): 
                    maxLength = max(maxLength,len(a)*len(b)) 
        return maxLength
                
    def NoCommonChar(self,s,t):
        Aplbatic = [False] * 26 
        if len(s) > len(t):
            s,t = t,s 
        for e in s:
            Aplbatic[ord(e)-97] = True
        for e in t:
            if Aplbatic[ord(e)-97]:
                return False  
        return True 
        """
        """  ---- Time Limit Exceeded ----
        if len(s)>len(t):
            s,t =t,s
        for a in s:
            if a in t:
                return True
        return False 
        """ 

                
