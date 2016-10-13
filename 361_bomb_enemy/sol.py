# no Liana solution


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        res, row_hits, col_hits = 0, 0, [0] * n
        for i in xrange(m):
            for j in xrange(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    row_hits, k = 0, j
                    while k < n and grid[i][k] != 'W':
                        row_hits += int(grid[i][k] == 'E')
                        k += 1

                if i == 0 or grid[i - 1][j] == 'W':
                    col_hits[j], k = 0, i
                    while k < m and grid[k][j] != 'W':
                        col_hits[j] += int(grid[k][j] == 'E')
                        k += 1

                if grid[i][j] == '0':
                    res = max(res, row_hits + col_hits[j])
        return res

sol = Solution()
print sol.maxKilledEnemies(["0E00", "E0WE", "0E00"])
