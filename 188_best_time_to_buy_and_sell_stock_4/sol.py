# no Liana solution


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2 or k == 0:
            return 0
        if k >= len(prices) / 2:
            profit = 0
            for i in xrange(1, len(prices)):
                profit += max(0, prices[i] - prices[i - 1])
            return profit

        INF = float('inf')
        buy = [-INF for _ in range(k)]
        sell = [0 for _ in range(k)]

        for p in prices:
            buy[0] = max(buy[0], -p)
            sell[0] = max(sell[0], buy[0] + p)
            for i in xrange(1, k):
                buy[i] = max(buy[i], sell[i - 1] - p)
                sell[i] = max(sell[i], buy[i] + p)
        return sell[-1]
