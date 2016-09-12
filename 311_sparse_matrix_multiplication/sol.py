# no Liana solution


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B or len(A[0]) != len(B):
            return None
        m, n, l = len(A), len(A[0]), len(B[0])
        res = [[0 for _ in xrange(l)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if A[i][j]:
                    for k in xrange(l):
                        if B[j][k]:
                            res[i][k] += A[i][j] * B[j][k]
        return res
