class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        INT_MAX = 2147483647
        maxPro = 0
        minPrice = INT_MAX
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPro = max(maxPro, prices[i] - minPrice)
        return maxPro

    def maxProfit_self(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        INF = float('inf')
        min_price = INF
        for p in prices:
            min_price = min(min_price, p)
            result = max(result, p - min_price)
        return result
