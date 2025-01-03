class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        def getLargerNeighbors(matrix, i,j):
            largerNieghbors = []
            cur = matrix[i][j]
            if i > 0 and matrix[i-1][j] > cur:
                largerNieghbors.append((i-1, j))
            if j > 0 and matrix[i][j-1] > cur:
                largerNieghbors.append((i, j-1))
            if i < row-1 and matrix[i+1][j] > cur:
                largerNieghbors.append((i+1, j))
            if j < col-1 and matrix[i][j+1] > cur:
                largerNieghbors.append((i, j+1))
            return largerNieghbors
        
        listLargerNieghbors = {}
        sorted_values = [] # each value and its indices in the matrix
        for i in range(row):
            for j in range(col):
                sorted_values.append((matrix[i][j], i, j))
                listLargerNieghbors[(i, j)] = getLargerNeighbors(matrix, i,j)
        
        # print(listLargerNieghbors)
        sorted_values.sort(key=lambda x: x[0])
        started = set() # do not contain the starting point of the longest path
        dp_table = {}
        def dfs(i, j):
            if (i, j) in dp_table:
                return dp_table[(i, j)]
            res = 1
            if len(listLargerNieghbors[(i, j)]) == 0:
                return res
            else:
                for ni, nj in listLargerNieghbors[(i, j)]:
                    started.add((ni,nj))
                    res = max(res, 1 + dfs(ni, nj))
            dp_table[(i, j)] = res
            return res
        
        final_res = 1
        for s in sorted_values:
            _, i, j = s
            if (i,j) not in started:
                final_res = max(final_res, dfs(i,j) )
        return final_res