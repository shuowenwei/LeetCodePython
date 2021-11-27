# 这个算法技巧的时间复杂度是 O(N)，比字符串暴力算法要高效得多。

def slidingWindow(s, t): 
    need = {}
    windown = {}

    need = {c:0 for c in t}
    left = 0
    right = 0
    valid = 0 
    while right < len(s):
        # // c 是将移入窗口的字符
        c = s[right]
        # // 右移窗口
        right += 1
        # // 进行窗口内数据的一系列更新
        ... 

        # /*** debug 输出的位置 ***/
        print(f"window: [%d, %d)\n", left, right) 
        # /********************/

        while (window needs shrink):
            # // d 是将移出窗口的字符
            d = s[left]
            # // 左移窗口
            left += 1 
            # // 进行窗口内数据的一系列更新
