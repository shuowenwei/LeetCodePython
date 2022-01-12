# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/house-robber-iii/

https://labuladong.gitee.io/algo/3/25/95/
https://mp.weixin.qq.com/s/z44hk0MW14_mAQd7988mfw

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
        dp_table = {}
        def dp(root):
            if root is None:
                return 0
            if root in dp_table:
                return dp_table[root]
            res = 0 
            # rob this root 
            if root.left and root.right:
                intRob = root.val + dp(root.left.left) + dp(root.left.right) + dp(root.right.left) + dp(root.right.right)
            elif root.left:
                intRob = root.val + dp(root.left.left) + dp(root.left.right)
            elif root.right:
                intRob = root.val + dp(root.right.left) + dp(root.right.right)
            else:
                intRob = root.val
            # don't rob this root
            intNotRob = dp(root.left) + dp(root.right)
            res = max(intRob, intNotRob)
            dp_table[root] = res 
            return res
        
        return dp(root)