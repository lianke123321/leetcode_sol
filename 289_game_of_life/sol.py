# no Liana solution


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                count = 0
                for x in xrange(max(i - 1, 0), min(i + 2, m)):
                    for y in xrange(max(j - 1, 0), min(j + 2, n)):
                        count += board[x][y] & 1
                if count == 3 or count - (board[i][j] & 1) == 3:
                    board[i][j] |= 2

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1

test = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]
sol = Solution()
sol.gameOfLife(test)
print test
