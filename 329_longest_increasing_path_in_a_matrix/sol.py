# no Liana solution


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n, res = len(matrix), len(matrix[0]), 0
        dp = [[None for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                res = max(res, self.dfs(dp, matrix, i, j))
        return res

    def dfs(self, dp, matrix, i, j):
        if not dp[i][j]:
            tmp = [0]
            if i > 0 and matrix[i - 1][j] > matrix[i][j]:
                tmp.append(self.dfs(dp, matrix, i - 1, j))
            if i < len(matrix) - 1 and matrix[i + 1][j] > matrix[i][j]:
                tmp.append(self.dfs(dp, matrix, i + 1, j))
            if j > 0 and matrix[i][j - 1] > matrix[i][j]:
                tmp.append(self.dfs(dp, matrix, i, j - 1))
            if j < len(matrix[0]) - 1 and matrix[i][j + 1] > matrix[i][j]:
                tmp.append(self.dfs(dp, matrix, i, j + 1))

            dp[i][j] = max(tmp) + 1
        return dp[i][j]

matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
sol = Solution()
print sol.longestIncreasingPath(matrix)
