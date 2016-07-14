class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(t)
        n = len(s)
        if m > n:
            return 0
        path = [[] for i in range(m + 1)]
        for i in range(0, m + 1):
            if i == 0:
                for j in range(0, n + 1):
                    path[i].append(1)
            else:
                for j in range(0, n + 1):
                    path[i].append(0)

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                path[i][j] = path[i][j - 1]
                if t[i - 1] == s[j - 1]:
                    path[i][j] += path[i - 1][j - 1]
        # print path
        return path[m][n]

    def numDistinct_self(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t) or (len(s) == len(t) and s != t):
            return 0

        dp = [[0 for _ in xrange(len(t) + 1)] for _ in xrange(len(s) + 1)]

        for i in xrange(len(s) + 1):
            dp[i][0] = 1

        for i in xrange(1, len(s) + 1):
            for j in xrange(1, min(len(t) + 1, i + 1)):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]

sol = Solution()
print sol.numDistinct_self('ccc', 'c')
