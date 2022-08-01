# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-duplicate-letters/

https://labuladong.gitee.io/algo/2/21/62/
https://mp.weixin.qq.com/s/Yq49ZBEW3DJx6nXk1fMusw

LC316==LC1081
monotonic stack
"""
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # ord('a') --> 97
        stack = []
        isInStack = set()
        charCount = {}
        for e in s: 
            if e in charCount:
                charCount[e] += 1
            else:
                charCount[e] = 1
        for e in s:
            charCount[e] -= 1 # // 每遍历过一个字符，都将对应的计数减一
            if e in isInStack:
                continue
            while len(stack) > 0 and ord(stack[-1]) > ord(e):
                if charCount[stack[-1]] == 0: # debug! 
                    # // 若之后不存在栈顶元素了，则停止 pop
                    break
                else:
                    # // 若之后还有，则可以 pop
                    tmp = stack.pop()
                    isInStack.remove(tmp)
                
            stack.append(e)
            isInStack.add(e)
            
        return ''.join(stack)

s = "bcabc"
obj = Solution()
obj.removeDuplicateLetters(s)
