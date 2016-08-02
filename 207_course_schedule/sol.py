# no Liana solution


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.adj = [set() for _ in xrange(numCourses)]
        self.visit = [0] * numCourses
        for i, j in prerequisites:
            self.adj[i].add(j)

        for i in xrange(numCourses):
            if not self.dfs(i):
                return False
        return True

    def dfs(self, i):
        if self.visit[i] == -1:
            return False
        elif self.visit[i] == 1:
            return True

        self.visit[i] = -1
        for j in self.adj[i]:
            if not self.dfs(j):
                return False
        self.visit[i] = 1
        return True
