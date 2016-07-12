# no Liana solution


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        INF = float('inf')
        dp = [0] + [INF] * amount
        for i in xrange(1, amount + 1):
            dp[i] = min([dp[i - c] if i >= c else INF for c in coins]) + 1

        return dp[amount] if dp[amount] != INF else -1
