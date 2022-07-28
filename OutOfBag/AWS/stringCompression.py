
import collections

def strCompression(s, k):
    if k <= 1:
        return 0 
    if k > len(s):
        return s
    slow, fast = 0, k-1
    q = collections.deque(s[slow:fast+1])
    # print(q)
    while fast < len(s):
        if len(set(q)) == 1:
            new_string = s[:slow] + s[fast+1:]
            return strCompression(new_string, k)
        else:
            fast += 1
            slow += 1
            q.popleft()
            q.append(s[fast])

input = 'abbcccb'
k = 3
print(strCompression(input, k))


input = 'abbccccbbaaabbbbb'
k = 4
print(strCompression(input, k))