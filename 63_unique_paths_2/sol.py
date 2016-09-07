class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(0, n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        for j in range(1, m):
            if obstacleGrid[j][0] == 0:
                dp[j][0] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePathsWithObstacles_self(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0 or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        dp[0][0] = 1

        for i in xrange(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for j in xrange(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                if obstacleGrid[i - 1][j] != 1:
                    dp[i][j] += dp[i - 1][j]
                if obstacleGrid[i][j - 1] != 1:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]

sol = Solution()
print sol.uniquePathsWithObstacles_self([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
