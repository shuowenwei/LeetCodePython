# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

https://labuladong.gitee.io/algo/2/18/28/

solution link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74395/Neat-python-solution-in-both-DFS-and-BFS

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    from collections import deque
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # BFS 
        if root is None:
            return ''
        q = deque()
        
        q.append(root)
        res = []
        while len(q) > 0:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                if cur is None:
                    res.append('')
                else:
                    res.append(str(cur.val)) 
                    q.append(cur.left)
                    q.append(cur.right)
        print(res)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        listVals = data.split(',')
        root = TreeNode(int(listVals[0]))
        cur_pos = 1
        
        q = deque()
        q.append(root)
        while len(q) > 0: 
            cur = q.popleft()
            if listVals[cur_pos] != '': 
                cur.left = TreeNode(int(listVals[cur_pos]))
                q.append(cur.left)
            cur_pos += 1 
            if listVals[cur_pos] != '': 
                cur.right = TreeNode(int(listVals[cur_pos]))
                q.append(cur.right)
            cur_pos += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


################################################################################################################
################################################################################################################

# doesn't work when the tree has duplicated values: [3,2,4,3]:
#      3
#    /  \ 
#   2    4
#  /
# 3 
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder = []
        inorder = []
        def traverse(root):
            if root is None:
                return
            preorder.append(root.val)
            traverse(root.left)
            inorder.append(root.val)
            traverse(root.right)
        traverse(root)
        # print(preorder) # list of integers, need to convert to str first
        # print(inorder)
        res = ','.join([str(val) for val in preorder]) + '||' + ','.join([str(val) for val in inorder])
        print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '||':
            return None
        preorder, inorder = data.split('||')[0].split(','), data.split('||')[1].split(',')
        # print(preorder, type(preorder))
        # print(inorder, type(inorder))
        def reconstruction(preorder, inorder):
            if len(inorder) == 0: 
                return None 
            rootVal = preorder.pop(0)
            root = TreeNode(int(rootVal))
            indexRootValInorder = inorder.index(rootVal)
            root.left = reconstruction(preorder, inorder[0 : indexRootValInorder])
            root.right = reconstruction(preorder, inorder[indexRootValInorder + 1 : ])
            return root
        root = reconstruction(preorder, inorder)
        return root 
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# PS：一般语境下，单单前序遍历结果是不能还原二叉树结构的，因为缺少空指针的信息，
# 至少要得到前、中、后序遍历中的两种才能还原二叉树。
# 但是这里的 node 列表包含空指针的信息，所以只使用 node 列表就可以还原二叉树。

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder = []
        def traverse(root):
            if root is None:
                preorder.append('#')
                return 
            preorder.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return ','.join([str(val) for val in preorder])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        preorder = data.split(',')
        
        def reconstruction(preorder):
            rootVal = preorder.pop(0)
            if rootVal == '#':
                return None 
            root = TreeNode(int(rootVal))
            root.left = reconstruction(preorder)
            root.right = reconstruction(preorder)
            return root
        root = reconstruction(preorder)
        return root 
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        postorder = []
        def traverse(root):
            if root is None:
                postorder.append('#')
                return
            traverse(root.left)
            traverse(root.right)
            postorder.append(root.val)
        traverse(root)
        return ','.join([str(val) for val in postorder])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        postorder = data.split(',')
        
        def reconstruction(postorder):
            rootVal = postorder.pop()
            if rootVal == '#':
                return None 
            root = TreeNode(int(rootVal))
            root.right = reconstruction(postorder)
            root.left = reconstruction(postorder)
            return root
        root = reconstruction(postorder)
        return root 
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))