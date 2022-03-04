# https://www.1point3acres.com/bbs/thread-841619-1-1.html
# 第五轮: 带括号的字母四则运算比如a+2(b-a)输出2b-a，a+2a(b+c) = a+2ab+2ac。用hashmap+stack
# ??LC726??, LC394

import collections
def evaluateString(s):
    stack = []
    dict_element2count = collections.defaultdict(int)
    element = ''
    coef = 1 
    coef_string = ''
    num = 0
    sign = '+'
    for i, char in enumerate(s):
        if char.isdigit():
            num += num*10 + int(char)
        elif char == '(':
            stack.append(max(num, 1))
            coef = coef * max(num, 1)
            coef_string = element
            element = ''
            num = 0
        elif char.islower():
            element += char
        # elif (not char.isdigit() and char != ' ') or i == len(s) - 1:
        elif char in ('+', '-') or i == len(s) - 1:
            if sign == '+':
                # if coef_string != '':
                dict_element2count[coef_string+element] += max(num, 1) * coef 
                # else:
                #     dict_element2count[element] += max(num, 1) * coef 
            elif sign == '-':
                # if coef_string != '':
                dict_element2count[coef_string+element] += -max(num, 1) * coef 
                # else:
                #     dict_element2count[element] += -max(num, 1) * coef
            element = ''
            sign = char
            num = 0
        elif char == ')':
            coef = 1
            coef_string = ''
            num = 0
        # print(stack, element, dict_element2count)
    print(dict_element2count)
    return ''.join(str('+' if v > 0 else '-')+str(v if abs(v) > 1 else '')+k for k,v in sorted(dict_element2count.items()))

s = 'a+2(b-a)'
# s = 'a+2a(b-c)'
print(evaluateString(s))
