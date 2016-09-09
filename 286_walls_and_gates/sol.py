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
            if row > 0 and rooms[row - 1][col] == 2147483647:
                rooms[row - 1][col] = rooms[row][col] + 1
                queue.appendleft((row - 1, col))
            if row < n - 1 and rooms[row + 1][col] == 2147483647:
                rooms[row + 1][col] = rooms[row][col] + 1
                queue.appendleft((row + 1, col))
            if col > 0 and rooms[row][col - 1] == 2147483647:
                rooms[row][col - 1] = rooms[row][col] + 1
                queue.appendleft((row, col - 1))
            if col < m - 1 and rooms[row][col + 1] == 2147483647:
                rooms[row][col + 1] = rooms[row][col] + 1
                queue.appendleft((row, col + 1))
