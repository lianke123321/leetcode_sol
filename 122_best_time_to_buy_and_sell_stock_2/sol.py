# no Liana solution


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        count = len(prices)

        if count < 2:
            return 0

        dp = [0 for _ in xrange(count)]

        for i in xrange(1, count):
            if prices[i] >= prices[i - 1]:
                dp[i] = dp[i - 1] + (prices[i] - prices[i - 1])
            else:
                dp[i] = dp[i - 1]

        return dp[-1]
