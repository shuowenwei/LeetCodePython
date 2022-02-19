# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

LC235, LC236, LC1650
LC1650, LC160, LC142
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, parent = None):
        self.val = x
        self.parent = parent
        #     3
        #    / \
        #   5   8
        #  / \
        # 6   2
        #    / \
        #   7   4  
root = TreeNode(3)
node5 = TreeNode(5, root)
node8 = TreeNode(8, root)
node6 = TreeNode(6, node5)
node2 = TreeNode(2, node5)
node7 = TreeNode(7, node2)
node4 = TreeNode(4, node2)

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        head_p = p
        head_q = q 
        while head_p.parent and head_q.parent:
            head_p = head_p.parent
            head_q = head_q.parent

        if head_p.parent is None:
            head_p.parent = p
            slow, fast, third = q, q, q

        if head_q.parent is None:
            head_q.parent = q
            slow, fast, third = p, p, p
        
        while True:
            fast = fast.parent.parent
            slow = slow.parent 
            if fast == slow:
                break
        
        while third != slow:
            third = third.parent
            slow = slow.parent
        return slow.val
    
    # refer to LC160
    def lowestCommonAncestor_LC160(self, p, q):
        head_p, head_q = p, q
        while p != q: 
            if p is None:
                p = head_q
            else:
                p = p.parent
            if q is None:
                q = head_p 
            else:
                q = q.parent
        return head_p.val

sol = Solution()
print(sol.lowestCommonAncestor(node6, node7))
print(sol.lowestCommonAncestor_LC160(node6, node7))

"""     if TreeNode has left and right child
        root = p
        while root.parent != None:
            root = root.parent
        
        # refer to KC235
        def helper(root, p, q):
            if root in (None, p, q):
                return root # None or p or q exists in the tree? 
            leftLCA = self.helper(root.left, p, q)
            rightLCA = self.helper(root.right, p, q)
            # do sth in post order
            if leftLCA and rightLCA:
                return root
            elif leftLCA: # and rightLCA is None:
                return leftLCA 
            elif rightLCA: # and leftLCA is None:
                return rightLCA
            else: # both leftLCA and rightLCA are None
                return None #leftLCA or rightLCA
            
        return helper(root, p, q)
"""