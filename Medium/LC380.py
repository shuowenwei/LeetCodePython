# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/insert-delete-getrandom-o1/

solution: https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python

https://labuladong.gitee.io/algo/2/21/61/

对于 getRandom 方法，如果想「等概率」且「在 O(1) 的时间」取出元素，一定要满足：底层用数组实现，且数组必须是紧凑的。
这样我们就可以直接生成随机数作为索引，从数组中取出该随机索引对应的元素，作为随机元素。
但如果用数组存储元素的话，插入，删除的时间复杂度怎么可能是 O(1) 呢？
可以做到！对数组尾部进行插入和删除操作不会涉及数据搬移，时间复杂度是 O(1)。
所以，如果我们想在 O(1) 的时间删除数组中的某一个元素 val，可以先把这个元素交换到数组的尾部，然后再 pop 掉。
交换两个元素必须通过索引进行交换对吧，那么我们需要一个哈希表 valToIndex 来记录每个元素值对应的索引。

LC380, LC710
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.val2index = {}
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val2index:
            return False
        self.nums.append(val) # insert to the tail 
        self.val2index[val] = len(self.nums) - 1 # index is length - 1 
        return True 
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val2index:
            return False
        
        removeIndex = self.val2index[val]
        lastValIndex = self.val2index[self.nums[-1]]
        
        self.nums[removeIndex] = self.nums[-1]
        self.val2index[self.nums[-1]] = removeIndex
        self.nums.pop()
        del self.val2index[val]
        return True 

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random 
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()