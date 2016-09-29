# no Liana solution


from collections import deque


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        queue = deque()
        m, n = len(rooms[0]), len(rooms)
        for i in xrange(n):
            for j in xrange(m):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            top = queue.pop()
            row, col = top[0], top[1]
            for r, c in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                if 0 <= r < n and 0 <= c < m and rooms[r][c] == 2147483647:
                    rooms[r][c] = rooms[row][col] + 1
                    queue.appendleft((r, c))
