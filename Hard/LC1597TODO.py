# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

https://leetcode.ca/all/1597.html
refer to https://leetcode.ca/2020-04-14-1597-Build-Binary-Expression-Tree-From-Infix-Expression/
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
            print('char',char)
            if char == '(':
                operatorStack.append(char)
            elif char.isdigit():
                newNode = Node(char)
                nodeStack.append(newNode)
            elif char == ')':
                while operatorStack[-1] != '(':
                    self.combine(operatorStack, nodeStack)
                checkIfIsLeft = operatorStack.pop() # pop out '('
                assert checkIfIsLeft == '(', f'error here: {checkIfIsLeft}'
            else: # char is in '+-*/'
                while len(operatorStack) > 0 and dctOpertor2Priority[operatorStack[-1]] >= dctOpertor2Priority[char]: # // @note: must be >=, for test case "1+2+3+4+5"
                    self.combine(operatorStack, nodeStack)
                operatorStack.append(char)
            print('operation stack', operatorStack)
            print('node values', [n.val for n in nodeStack])
            
        while len(nodeStack) > 1:
            self.combine(operatorStack, nodeStack)
            print('final operation stack', operatorStack)
            print('final node values', [n.val for n in nodeStack])
        return nodeStack[-1]

sol = Solution()
# s = '2-3/(5*2)+1'
s = "3*4-2*5"
res = sol.exoTree(s)
print(res.val)

def traverseTree(root):
    if root is None:
        print('null')
        return
    print(root.val)
    traverseTree(root.left)
    traverseTree(root.left)

traverseTree(res)