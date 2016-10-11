# no Liana solution


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in xrange(1, len(row)):
                row[col] += row[col - 1]
        self.matrix = matrix

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        orig = self.matrix[row][col]
        if col > 0:
            orig -= self.matrix[row][col - 1]

        diff = orig - val
        for i in xrange(col, len(self.matrix[0])):
            self.matrix[row][i] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in xrange(row1, row2 + 1):
            res += self.matrix[i][col2]
            if col1 > 0:
                res -= self.matrix[i][col1 - 1]
        return res

# Your NumMatrix object will be instantiated and called as such:
matrix = [[2, 4], [-3, 5]]
numMatrix = NumMatrix(matrix)
numMatrix.update(0, 1, 3)
numMatrix.update(1, 1, -3)
numMatrix.update(0, 1, 1)
print numMatrix.sumRegion(0, 0, 1, 1)
