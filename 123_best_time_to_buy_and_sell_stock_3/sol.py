# no Liana solution


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        INF = float('inf')
        sell1, sell2 = 0, 0
        buy1, buy2 = -INF, -INF
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
        return sell2

sol = Solution()
print sol.maxProfit([7, 6, 5, 4])
