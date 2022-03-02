"""
https://leetcode.com/discuss/interview-question/425337/google-phone-screen-find-value-that-minimizes-expression

You are given a function F, which maps non-negative integers to non-negative integers. You know that F is monotonically increasing: 
if x > y, then F(x) > F(y).

Write code which given such a function F, and an integer y, quickly finds the value x such that | F(x) - y | is minimized.
"""

def f(x):
    pass 
def minExpression(f, y):
    
    # left = - 2**32 - 1
    # right = 2**32 + 1
    
    right = 1
    while f(right) < y:
        right = right * 2
    left = right // 2
    
    while left <= right:
        mid = (left + right) // 2 
        if f(mid) < y:
            left = mid + 1
        else:
            right = mid - 1
    # Now f(left) >= y, f(right) < y
    return min(left, right, key=lambda x: abs(f(x) - y))
