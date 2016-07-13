# no Liana solution


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0

        k = len(costs[0])
        min_1, min_2 = -1, -1

        for i in range(n):
            last_1, last_2 = min_1, min_2
            min_1, min_2 = -1, -1
            for j in range(k):
                if j == last_1:
                    costs[i][j] += costs[i - 1][last_2] if last_2 != -1 else 0
                else:
                    costs[i][j] += costs[i - 1][last_1] if last_1 != -1 else 0

                # update min_1 and min_2 indices
                if min_1 == -1 or costs[i][min_1] > costs[i][j]:
                    min_2, min_1 = min_1, j
                elif min_2 == -1 or costs[i][min_2] > costs[i][j]:
                    min_2 = j
        return costs[-1][min_1]
