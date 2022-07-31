# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

"""
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def combine(self, opsStack, ndStack):
        root = Node(opsStack.pop())
        # first poped is the right child 
        root.right = ndStack.pop()
        root.left = ndStack.pop()
        ndStack.append(root)
        
    def exoTree(self, s):
        dctOpertor2Priority = { '(': 1, 
                                '+': 2,
                                '-': 2,
                                '*': 3,
                                '/': 3}
        
        operatorStack = []
        nodeStack = []
        for char in s: 
            # print(char, 'char')
            if char == '(':
                operatorStack.append(char)
            elif char.isdigit():
                newNode = Node(int(char))
                nodeStack.append(newNode)
            elif char == ')':
                while operatorStack[-1] != '(':
                    self.combine(operatorStack, nodeStack)
                checkIfIsLeft = operatorStack.pop() # pop out '('
                assert checkIfIsLeft == '(', f'error here: {checkIfIsLeft}'
            else: # char is in '+-*/'
                while len(operatorStack) > 0 and dctOpertor2Priority[operatorStack[-1]] > dctOpertor2Priority[char]:
                    self.combine(operatorStack, nodeStack)
                operatorStack.append(char)
        
        while len(nodeStack) > 1:
            self.combine(operatorStack, nodeStack)
        return nodeStack[-1]

sol = Solution()
s = '2-3/(5*2)+1'
s = "3*4-2*5"
res = sol.exoTree(s)
print(res.val)

def traverseTree(root):
    if root is None:
        return 
    traverseTree(root.left)
    print(root.val)
    traverseTree(root.left)

traverseTree(res)