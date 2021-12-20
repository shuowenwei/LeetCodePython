# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-frequency-stack/

https://labuladong.gitee.io/algo/2/20/45/

LC146, LC460, LC895

"""
class FreqStack(object):
    def __init__(self):
        import collections
        self.maxFreq = 0
        self.val2Freq = dict()
        self.freq2Vals = collections.defaultdict(list)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.val2Freq: 
            self.val2Freq[val] += 1
        else: 
            self.val2Freq[val] = 1
            
        newFreq = self.val2Freq[val]
        self.maxFreq = max(self.maxFreq, newFreq)

        self.freq2Vals[newFreq].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.freq2Vals[self.maxFreq].pop()
        self.val2Freq[val] -= 1
        if len(self.freq2Vals[self.maxFreq]) == 0: 
            self.maxFreq -= 1 
        return val 
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
