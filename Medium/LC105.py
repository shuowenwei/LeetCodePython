# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        # solution 1: (modify preorder as we go) 
        """
        if len(inorder) == 0: # when len(preorder) == 0, continue 
            return None
        rootVal = preorder.pop(0)
        root = TreeNode(rootVal)
        indexRootValInorder = inorder.index(rootVal) # root val: 3, index in inorder: 1 
                
        root.left = self.buildTree(preorder, inorder[0:indexRootValInorder])
        root.right = self.buildTree(preorder, inorder[indexRootValInorder+1:])
        return root 
        """

        # solution 2:  (get absolute index of root each time) 
        # *Start and *End are all indices in the list: for a lit with length=5, its indices are: 0,1,2,3,4 
        preStart, preEnd = 0, len(preorder)-1
        inStart, inEnd = 0, len(inorder)-1
        
        def helper(preorder, preStart, preEnd, \
                   inorder, inStart, inEnd): 
            if preStart > preEnd or inStart > inEnd:
                return None
            # print('pre', preStart, preEnd, 'in', inStart, inEnd)
            rootVal = preorder[preStart]
            root = TreeNode(rootVal)
            indexRootValInorder = inorder.index(rootVal) # root val: 3, index in inorder: 1
            numLeftNodes = indexRootValInorder - inStart 

            root.left = helper(preorder, preStart+1, preStart+numLeftNodes, \
                               inorder, inStart, indexRootValInorder-1)
            
            root.right = helper(preorder, preStart+1+numLeftNodes, preEnd, \
                                inorder, indexRootValInorder+1, inEnd)
            return root
        return helper(preorder, preStart, preEnd, inorder, inStart, inEnd)