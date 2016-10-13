# no Liana solution
from collections import deque


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        m, n, total = len(grid), len(grid[0]), sum(val for row in grid for val in row if val == 1)
        hits, dist_sum = [[0] * n for _ in xrange(m)], [[0] * n for _ in xrange(m)]

        def bfs(i, j):
            visited = [[False] * n for _ in xrange(m)]
            visited[i][j], count_building, q = True, 1, deque([(i, j, 0)])
            while q:
                X, Y, dist = q.popleft()
                for x, y in (X - 1, Y), (X + 1, Y), (X, Y - 1), (X, Y + 1):
                    if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                        visited[x][y] = True
                        if grid[x][y] == 0:
                            q.append((x, y, dist + 1))
                            hits[x][y] += 1
                            dist_sum[x][y] += (dist + 1)
                        elif grid[x][y] == 1:
                            count_building += 1
            return count_building == total

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1 and not bfs(i, j):
                    return -1

        return min([dist_sum[i][j] for i in xrange(m) for j in xrange(n)
                    if grid[i][j] == 0 and hits[i][j] == total] or [-1])

grid = [
    [1, 0, 2, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]
sol = Solution()
print sol.shortestDistance(grid)
