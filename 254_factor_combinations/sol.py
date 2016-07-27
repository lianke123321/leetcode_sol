# no Liana solution


class Solution(object):
    def __init__(self):
        self.result = []

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 3:
            return []
        self.dfs([], n, 2)
        return self.result

    def dfs(self, stack, n, i):
        while i * i <= n:
            if n % i == 0:
                self.result.append(stack + [i, n / i])
                self.dfs(stack + [i], n / i, i)
            i += 1

sol = Solution()
print sol.getFactors(23848713)
