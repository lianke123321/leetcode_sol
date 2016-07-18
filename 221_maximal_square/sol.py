class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        maxSize = 0
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            maxSize = max(maxSize, dp[0][j])
        for i in range(1, m):
            dp[i][0] = int(matrix[i][0])
            maxSize = max(maxSize, dp[i][0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSize = max(maxSize, dp[i][j])
        return maxSize * maxSize

    def maximalSquare_self(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        result = 0

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    result = max(result, dp[i][j])
        return result * result
