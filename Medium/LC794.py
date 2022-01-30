# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-tic-tac-toe-state/submissions/

LC794, LC348
"""
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        numX, numO = 0, 0
        eightWins = [board[0], board[1], board[2], 
                     board[0][0]+board[1][0]+board[2][0], 
                     board[0][1]+board[1][1]+board[2][1], 
                     board[0][2]+board[1][2]+board[2][2], 
                     board[0][0]+board[1][1]+board[2][2], board[0][2]+board[1][1]+board[2][0]]
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X': 
                    numX += 1
                if board[i][j] == 'O':
                    numO += 1
        # print(eightWins)
        # print(eightWins.count('XXX'))
        if eightWins.count('XXX') > 0 and eightWins.count('OOO') > 0:
            return False
        elif 'XXX' in eightWins and 'OOO' in eightWins:
            return False
        elif 'XXX' in eightWins:
            return numX -1 == numO
        elif 'OOO' in eightWins:
            return numX == numO
        elif numX < numO or numX - 1 > numO:
            return False
        # print(numX, numO)
        return True
        