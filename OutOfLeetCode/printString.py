
# https://www.1point3acres.com/bbs/thread-841619-1-1.html

# 输入x是1-4,y是2-6,z是3-7输出[1,2) x, [2,3) x,y, [3,4] x,y,z, (4,6] y,z, (6,7] z。
# 总体就是当区间的内容有变化的时候就打印一个区间还有内容，注意 [ 和 ( 表示是否包括。
                                                                                                             

def printString(dictChar2Interval):
    lstCharValueLeft = [[char, interval[0]] for char, interval in dictChar2Interval.items()]
    lstCharValueRight = [[char, interval[1]] for char, interval in dictChar2Interval.items()]
    lstCharValue = lstCharValueLeft + lstCharValueRight
    lstCharValue.sort(key = lambda x: x[1])
    print(lstCharValue)
    n = len(lstCharValue)
    res = []
    setChar = set()
    for i in range(n - 1):
        char, val = lstCharValue[i]
        nextChar, nextVal = lstCharValue[i + 1]
        left_sign = ''
        right_sign = '#'
        if char not in setChar:
            setChar.add(char)
            left_sign = '['
        else:
            setChar.remove(char)
            left_sign = '('
        inputChar = ','.join(sorted(list(setChar)))
        res.append(f'{left_sign}{val}, {nextVal}{right_sign} {inputChar}')
        
    print('res before:', res)
    for i in range(n - 2):
        # print(res[i + 1][0])
        if res[i + 1][0] == '[':
            res[i] = res[i].replace(right_sign, ')')
        if res[i + 1][0] == '(':
            res[i] = res[i].replace(right_sign, ']')
    res[-1] = res[-1].replace(right_sign, ']')
    print('res after:', res)
    print(', '.join(res))
    return res 

dictChar2Interval = {}
dictChar2Interval['x'] = [1, 4]
dictChar2Interval['y'] = [2, 6]
dictChar2Interval['z'] = [3, 7]

printString(dictChar2Interval)