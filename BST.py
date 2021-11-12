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

    # LC700 https://leetcode.com/problems/search-in-a-binary-search-tree/
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
    
    # LC450 https://leetcode.com/problems/delete-node-in-a-bst/
    # 情况 1：A 恰好是末端节点，两个子节点都为空，那么它可以当场去世了。
    # 情况 2：A 只有一个非空子节点，那么它要让这个孩子接替自己的位置。
    # 情况 3：A 有两个子节点，麻烦了，为了不破坏 BST 的性质，A 必须找到左子树中最大的那个节点，或者右子树中最小的那个节点来接替自己。我们以第二种方式讲解。
    def deleteNode(self, root, key):
        if root is None:
            return None 
        if root.val == key:
            if root.left is None and root.right is None:
                return None 
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else: # root.left is not None and root.right is not None:
                # First find the right most leaf of the left sub-tree
                rightmost_LeftSubTree = root.left 
                while rightmost_LeftSubTree.right:
                    rightmost_LeftSubTree = rightmost_LeftSubTree.right
                rightmost_LeftSubTree.right = root.right
                return root.left
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    # LC98 https://leetcode.com/problems/validate-binary-search-tree
    def isValidBST(self, root):
        def helper(root, floor, ceil): 
            if root is None:
                return True
            if root.val <= floor or root.val >= ceil:
                return False
            if root.left and root.left.val >= root.val:
                return False 
            if root.right and root.right.val <= root.val:
                return False
            else:
                return helper(root.left, floor, min(ceil, root.val)) and helper(root.right, max(floor, root.val), ceil)

        return helper(root, -2**31-1, 2**31+1)
