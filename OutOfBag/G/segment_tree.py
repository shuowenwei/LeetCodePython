"""
Range Minimum Query (Square Root Decomposition and Sparse Table)

https://www.geeksforgeeks.org/range-minimum-query-for-static-array/
A simple solution is to run a loop from qs to qe and find minimum element in given range. 
This solution takes O(n) time in worst case. 

Another solution is to create a 2D array where an entry [i, j] stores the minimum value in range arr[i..j]. 
Minimum of a given range can now be calculated in O(1) time, but preprocessing takes O(n^2) time. 
Also, this approach needs O(n^2) extra space which may become huge for large input arrays.
"""
# Python3 program to do range
# minimum query in O(1) time with
# O(n*n) extra space and O(n*n)
# preprocessing time.
MAX = 500

# lookup[i][j] is going to store
# index of minimum value in
# arr[i..j]
lookup = [[0 for j in range(MAX)]
			for i in range(MAX)]

# Structure to represent
# a query range
class Query:
	
	def __init__(self, L, R):
		
		self.L = L
		self.R = R

# Fills lookup array lookup[n][n]
# for all possible values
# of query ranges
def preprocess(arr, n):

	# Initialize lookup[][] for the
	# intervals with length 1
	for i in range(n):
		lookup[i][i] = i;

	# Fill rest of the entries in
	# bottom up manner
	for i in range(n):
		for j in range(i + 1, n):

			# To find minimum of [0,4],
			# we compare minimum
			# of arr[lookup[0][3]] with arr[4].
			if (arr[lookup[i][j - 1]] < arr[j]):
				lookup[i][j] = lookup[i][j - 1];
			else:
				lookup[i][j] = j;

# Prints minimum of given m
# query ranges in arr[0..n-1]
def RMQ(arr, n, q, m):

	# Fill lookup table for
	# all possible input queries
	preprocess(arr, n);

	# One by one compute sum of
	# all queries
	for i in range(m):

		# Left and right boundaries
		# of current range
		L = q[i].L
		R = q[i].R;

		# Print sum of current query range
		print("Minimum of [" + str(L) + ", " +
			str(R) + "] is " +
			str(arr[lookup[L][R]]))

# Driver code
if __name__ == "__main__":
	
	a = [7, 2, 3, 0, 5,
		10, 3, 12, 18]
	n = len(a)
	q = [Query(0, 4),
		Query(4, 7),
		Query(7, 8)]
	m = len(q)
	RMQ(a, n, q, m);


##########################################################################################################


# Python3 program for range minimum
# query using segment tree
import sys;
from math import ceil,log2;

INT_MAX = sys.maxsize;

# A utility function to get
# minimum of two numbers
def minVal(x, y) :
	return x if (x < y) else y;

# A utility function to get the
# middle index from corner indexes.
def getMid(s, e) :
	return s + (e - s) // 2;

""" A recursive function to get the
minimum value in a given range
of array indexes. The following
are parameters for this function.

	st --> Pointer to segment tree
	index --> Index of current node in the
		segment tree. Initially 0 is
		passed as root is always at index 0
	ss & se --> Starting and ending indexes
				of the segment represented
				by current node, i.e., st[index]
	qs & qe --> Starting and ending indexes of query range """
def RMQUtil( st, ss, se, qs, qe, index) :

	# If segment of this node is a part
	# of given range, then return
	# the min of the segment
	if (qs <= ss and qe >= se) :
		return st[index];

	# If segment of this node
	# is outside the given range
	if (se < qs or ss > qe) :
		return INT_MAX;

	# If a part of this segment
	# overlaps with the given range
	mid = getMid(ss, se);
	return minVal(RMQUtil(st, ss, mid, qs,
						qe, 2 * index + 1),
				RMQUtil(st, mid + 1, se,
						qs, qe, 2 * index + 2));

# Return minimum of elements in range
# from index qs (query start) to
# qe (query end). It mainly uses RMQUtil()
def RMQ( st, n, qs, qe) :

	# Check for erroneous input values
	if (qs < 0 or qe > n - 1 or qs > qe) :
	
		print("Invalid Input");
		return -1;
	
	return RMQUtil(st, 0, n - 1, qs, qe, 0);

# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment tree st
def constructSTUtil(arr, ss, se, st, si) :

	# If there is one element in array,
	# store it in current node of
	# segment tree and return
	if (ss == se) :

		st[si] = arr[ss];
		return arr[ss];

	# If there are more than one elements,
	# then recur for left and right subtrees
	# and store the minimum of two values in this node
	mid = getMid(ss, se);
	st[si] = minVal(constructSTUtil(arr, ss, mid,
									st, si * 2 + 1),
					constructSTUtil(arr, mid + 1, se,
									st, si * 2 + 2));
	
	return st[si];

"""Function to construct segment tree
from given array. This function allocates
memory for segment tree and calls constructSTUtil()
to fill the allocated memory """
def constructST( arr, n) :

	# Allocate memory for segment tree

	# Height of segment tree
	x = (int)(ceil(log2(n)));

	# Maximum size of segment tree
	max_size = 2 * (int)(2**x) - 1;

	st = [0] * (max_size);

	# Fill the allocated memory st
	constructSTUtil(arr, 0, n - 1, st, 0);

	# Return the constructed segment tree
	return st;

# Driver Code
if __name__ == "__main__" :

	arr = [1, 3, 2, 7, 9, 11];
	n = len(arr);

	# Build segment tree from given array
	st = constructST(arr, n);

	qs = 1; # Starting index of query range
	qe = 5; # Ending index of query range

	# Print minimum value in arr[qs..qe]
	print("Minimum of values in range [", qs,
		",", qe, "]", "is =", RMQ(st, n, qs, qe));

# This code is contributed by AnkitRai01
