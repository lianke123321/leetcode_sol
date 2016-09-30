class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # Traverse Right
            for i in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][i])
            rowBegin += 1
            # Traverse Down
            for i in range(rowBegin, rowEnd + 1):
                res.append(matrix[i][colEnd])
            colEnd -= 1
            if rowBegin <= rowEnd:
                # Traverse Left
                i = colEnd
                while i >= colBegin:
                    res.append(matrix[rowEnd][i])
                    i -= 1
                rowEnd -= 1
            if colBegin <= colEnd:
                # Traver Up
                i = rowEnd
                while i >= rowBegin:
                    res.append(matrix[i][colBegin])
                    i -= 1
                colBegin += 1
        return res

    def spiralOrder_self(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        res, i, j = [], 0, 0
        seq, p = [[0, 1], [1, 0], [0, -1], [-1, 0]], 0
        while True:
            if not 0 <= i < m or not 0 <= j < n or matrix[i][j] == '#':
                break
            res.append(matrix[i][j])
            matrix[i][j] = '#'
            next_i, next_j = i + seq[p][0], j + seq[p][1]
            if not 0 <= next_i < m or not 0 <= next_j < n or matrix[next_i][next_j] == '#':
                p = (p + 1) % 4
            i += seq[p][0]
            j += seq[p][1]
        return res

sol = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print sol.spiralOrder_self(matrix)
