# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/house-robber-iii/

labuladong: https://mp.weixin.qq.com/s/z44hk0MW14_mAQd7988mfw

LC198, LC213, LC337

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memo = {}
        def dp(root):
            if root is None:
                return 0
            if root in memo:
                return memo[root]
            # // 抢，然后去下下家
            if root.left and root.right: 
                intRob = root.val + dp(root.left.left) +  dp(root.left.right) + dp(root.right.left) + dp(root.right.right)
            elif root.left: 
                intRob = root.val + dp(root.left.left) +  dp(root.left.right)
            elif root.right:
                intRob = root.val + dp(root.right.left) + dp(root.right.right)
            else:
                intRob = root.val
            # // 不抢，然后去下家
            intNotRob = dp(root.left) + dp(root.right)
            res = max(intNotRob, intRob)
            memo[root] = res             
            return res         
        return dp(root)
