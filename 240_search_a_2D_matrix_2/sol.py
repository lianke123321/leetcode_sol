# no Liana solution

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])

        r = row - 1
        c = 0
        while r >= 0 and c < col:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                c += 1
            else:
                r -= 1
        return False
