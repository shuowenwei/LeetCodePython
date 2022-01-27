# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/text-justification/

LC1592, LC68
"""
class Solution(object):
    def reorderSpaces(self, tokens, maxWidth):
        """
        :type text: str
        :rtype: str
        """
        # tokens = text.split()
        if len(tokens) == 1:        
            return tokens[0] + ' '*(maxWidth - len(tokens[0]))
        
        numSpaces = maxWidth - sum(len(t) for t in tokens)
        gapLength = numSpaces / (len(tokens)-1)
        extraSpaces = numSpaces % (len(tokens)-1)
        leftGap = gapLength
        if extraSpaces != 0:
            res = ''
            for i in range(extraSpaces):
                res += tokens[i] + ' '*(leftGap+1)
            res += (' '*gapLength).join(tokens[i+1:])
            return res
        else:
            return (' '*gapLength).join(tokens) 
    
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        cur_pipeline = []
        cur_length = 0
        n = len(words)
        for i in range(n):
            if len(words[i]) + cur_length + len(cur_pipeline) == maxWidth:
                cur_length += len(words[i])
                cur_pipeline.append(words[i])
                res.append(self.reorderSpaces(cur_pipeline, maxWidth))
                cur_pipeline = []
                cur_length = 0
            elif len(words[i]) + cur_length + len(cur_pipeline) > maxWidth:
                res.append(self.reorderSpaces(cur_pipeline, maxWidth))
                cur_length = len(words[i])
                cur_pipeline = [words[i]]
            else:
                cur_length += len(words[i])
                cur_pipeline.append(words[i])
        # if last pipeline not empty:
        if cur_pipeline:
            res.append(' '.join(cur_pipeline) + ' '*(maxWidth-len(' '.join(cur_pipeline) )))
        return res