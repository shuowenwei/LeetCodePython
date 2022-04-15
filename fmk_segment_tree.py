"""
https://www.geeksforgeeks.org/range-minimum-query-for-static-array/

Input:  arr[]   = {7, 2, 3, 0, 5, 10, 3, 12, 18};
        query[] = [0, 4], [4, 7], [7, 8]

Output: Minimum of [0, 4] is 0
        Minimum of [4, 7] is 3
        Minimum of [7, 8] is 12

"""
from math import ceil, log2
class SegmentTree(object):
# If n is a power of 2, then there are no dummy nodes. So the size of the segment tree is 2n-1 (n leaf nodes and n-1 internal nodes). 
# If n is not a power of 2, then the size of the tree will be 2*x – 1 where x is the smallest power of 2 greater than n. 
# For example, when n = 10, then size of array representing segment tree is 2*16-1 = 31. 
    def __init__(self, input_array):
        self.MAX_VALUE = float('inf')
        n = len(input_array)
        x = (int)(ceil(log2(n)))
        self.st_max_size = 2 * (int)(2**x) - 1 
        self.segment_tree = [self.MAX_VALUE] * self.st_max_size
        self.low = 0 
        self.high = n - 1 
        self.pos = 0 # root of the binary segment tree
        self.constructSegmentTree(input_array, self.segment_tree, self.low, self.high, self.pos)

    def constructSegmentTree(self, input_array, segment_tree, low, high, pos):
        if low == high:
            segment_tree[pos] = input_array[low]
            return
        mid = (low + high) // 2
        self.constructSegmentTree(input_array, segment_tree, low, mid, 2 * pos + 1)
        self.constructSegmentTree(input_array, segment_tree, mid + 1, high, 2 * pos + 2)
        # index 'pos' in segment_tree
        # left child: 2 * pos + 1
        # right child: 2 * pos + 2
        # its parent: (pos - 1)/2
        segment_tree[pos] = min(segment_tree[2 * pos + 1], segment_tree[2 * pos + 2])
        
    def rangeMinQuery(self, qLow, qHigh):
        return self.query(qLow, qHigh, self.low, self.high, self.pos)
    
    def query(self, qLow, qHigh, low, high, pos):
        if qLow <= low and qHigh >= high: # total overlap 
            return self.segment_tree[pos]
        if qLow > high or qHigh < low: # no overlap
            return self.MAX_VALUE
        mid = (low + high) // 2
        return min(self.query(qLow, qHigh, low, mid, 2 * pos + 1), 
                   self.query(qLow, qHigh, mid + 1, high, 2 * pos + 2))

input_array = [7, 2, 3, 0, 5, 10, 3, 12, 18]
st = SegmentTree(input_array)

print(st.segment_tree)
print(st.rangeMinQuery(0, 4))
print(st.rangeMinQuery(4, 7))
print(st.rangeMinQuery(7, 8))

# Output: Minimum of [0, 4] is 0
#         Minimum of [4, 7] is 3
#         Minimum of [7, 8] is 12