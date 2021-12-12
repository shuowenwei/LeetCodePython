# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/

https://labuladong.gitee.io/algo/2/18/22/

LC654, LC105, LC106 

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        """
        # solution 1: modify postorder as we go:
        if len(inorder) == 0: # when len(preorder) == 0, continue ???
            return None
        rootVal = postorder.pop()
        root = TreeNode(rootVal)
        indexRootValInorder = inorder.index(rootVal)
        root.right = self.buildTree(inorder[indexRootValInorder+1:], postorder)
        root.left = self.buildTree(inorder[:indexRootValInorder], postorder)
        return root 
        """
        # solution 2: get absoluate index of root each time 
        # *Start and *End are all indices in the list: for a lit with length=5, its indices are: 0,1,2,3,4 
        # preStart, preEnd = 0, len(preorder)-1
        postStart, postEnd = 0, len(postorder) -1 
        inStart, inEnd = 0, len(inorder)-1
        def helper(postorder, postStart, postEnd, \
                   inorder, inStart, inEnd): 
            if inStart > inEnd or postStart > postEnd:
                return None
            # print('post', postStart, postEnd, 'in', inStart, inEnd)
            rootVal = postorder[postEnd]
            root = TreeNode(rootVal)
            indexRootValInorder = inorder.index(rootVal) # root val: 3, index in inorder: 1
            numLeftNodes = indexRootValInorder - inStart 
            
            root.right = helper(postorder, postStart+numLeftNodes, postEnd-1, \
                               inorder, indexRootValInorder+1, inEnd)
            
            root.left = helper(postorder, postStart, postStart+numLeftNodes-1, \
                               inorder, inStart, indexRootValInorder-1)
            return root
        return helper(postorder, postStart, postEnd, inorder, inStart, inEnd)
        