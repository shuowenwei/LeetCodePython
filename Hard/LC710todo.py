# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/random-pick-with-blacklist/

https://labuladong.gitee.io/algo/2/21/61/

LC380, LC710
"""
class Solution(object):
    import random
    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        self.nums = [i for i in range(n)]
        self.val2index = {val:index for index,val in enumerate(self.nums)}
        self.numWhiteElement = n - len(blacklist)
        lastIndex = n-1
        for b in blacklist:
            # print('before', self.nums, self.val2index)
            if b == self.nums[lastIndex]:
                lastIndex -= 1
                continue
            indexB = self.val2index[b]
            # swap self.nums[lastIndex] and b and their indices 
            self.nums[indexB] = self.nums[lastIndex]
            self.val2index[self.nums[indexB]] = indexB
            
            self.nums[lastIndex] = b
            self.val2index[b] = lastIndex
            
            # swap self.nums[lastIndex] and b and their indices 
            # self.nums[lastIndex], self.nums[bIndex] = self.nums[bIndex], self.nums[lastIndex]
            # self.val2index[self.nums[lastIndex]] = lastIndex
            # self.val2index[self.nums[bIndex]] = bIndex

            lastIndex -= 1 
            print('after', self.nums, self.val2index)
            
    def pick(self):
        """
        :rtype: int
        """
        import random
        return random.choice(self.nums[:self.numWhiteElement])
        # n = random.randint(0, self.numWhite - 1)
        # return self.nums[n]
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()