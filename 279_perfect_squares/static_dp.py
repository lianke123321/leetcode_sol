# no Liana solution
from math import sqrt


class Solution(object):
    _dp = [0, 1]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            dp.append(min(dp[-i ** 2] for i in xrange(1, int(sqrt(len(dp)))+1)) + 1)
        return dp[n]

sol = Solution()
print sol.numSquares(12)
print sol.numSquares(13)
print sol.numSquares(4703)
print sol.numSquares(5673)
