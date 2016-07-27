# no Liana solution


class Solution(object):
    def __init__(self):
        self.result = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return self.result
        self.dfs([], n, k)
        return self.result

    def dfs(self, stack, n, k):
        if k == 0:
            self.result.append(stack)

        for i in reversed(xrange(1, n + 1)):
            if k > i:
                break
            self.dfs(stack + [i], i - 1, k - 1)
