# no Liana solution


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return

        row, col = len(board), len(board[0])
        coordinate_stack = [xy for k in xrange(row + col)
                            for xy in (0, k), (row - 1, k), (k, 0), (k, col - 1)]

        while coordinate_stack:
            x, y = coordinate_stack.pop()
            if 0 <= x < row and 0 <= y < col and board[x][y] == 'O':
                board[x][y] = 'S'
                coordinate_stack += (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)

        for i in xrange(row):
            for j in xrange(col):
                board[i][j] = 'O' if board[i][j] == 'S' else 'X'
