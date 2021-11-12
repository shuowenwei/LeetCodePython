# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # LC700
    def searchBST(self, root, val):
        if root is None:
            return None 
        if val == root.val: 
            return root 
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    # LC701 https://leetcode.com/problems/insert-into-a-binary-search-tree/
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        # if val == root.val:
        #     BST 中一般不会插入已存在元素
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root