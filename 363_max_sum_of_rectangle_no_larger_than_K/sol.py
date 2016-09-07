# no Liana solution

import bisect


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def max_sum_no_greater_than_k(vals):
            max_sum = float('-inf')
            prefix_sum, prefix_sums = 0, [float('inf')]
            for val in vals:
                bisect.insort(prefix_sums, prefix_sum)
                prefix_sum += val
                i = bisect.bisect_left(prefix_sums, prefix_sum - k)
                max_sum = max(max_sum, prefix_sum - prefix_sums[i])
                if max_sum == k:
                    return max_sum
            return max_sum

        if len(matrix) == 0:
            return 0

        col, row = len(matrix[0]), len(matrix)
        result = float('-inf')
        for left in xrange(col):
            sums = [0] * row
            for right in xrange(left, col):
                # update accumulative sum for each row
                for i in xrange(row):
                    sums[i] += matrix[i][right]

                result = max(result, max_sum_no_greater_than_k(sums))
                if result == k:
                    return result
        return result

matrix = [
    [1, 0, 1],
    [0, -2, 3]
]
sol = Solution()
print sol.maxSumSubmatrix(matrix, 2)
