class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        """
        https://leetcode.com/discuss/20240/share-my-dp-solution
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        left = [0 for i in range(n)]
        right = [n for i in range(n)]
        height = [0 for i in range(n)]
        maxSize = 0
        for i in range(m):
            cur_left = 0
            cur_right = n
            for j in range(n):  # compute height (can do this from either side)
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(n):  # compute left (from left to right)
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            for j in range(n):  # compute right (from right to left)
                if matrix[i][n - 1 - j] == '1':
                    right[n - 1 - j] = min(right[n - 1 - j], cur_right)
                else:
                    right[n - 1 - j] = n
                    cur_right = n - 1 - j
            for j in range(n):  # compute the area of rectangle (can do this from either side)
                maxSize = max(maxSize, (right[j] - left[j]) * height[j])

        return maxSize

    def maximalRectangle_self(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        left, right, height = [0] * n, [n] * n, [0] * n
        result = 0

        for i in xrange(m):
            curr_left, curr_right = 0, n
            for j in xrange(n):
                if matrix[i][j] == '1':
                    # initialize height
                    height[j] += 1  # else it will still be 0

                    # initialize left
                    left[j] = max(left[j], curr_left)
                else:
                    curr_left = j + 1
                    height[j], left[j] = 0, 0

                # initialize right
                if matrix[i][n - 1 - j] == '1':
                    right[n - 1 - j] = min(right[n - 1 - j], curr_right)
                else:
                    curr_right = n - 1 - j
                    right[n - 1 - j] = n

            for j in xrange(n):
                result = max(result, (right[j] - left[j]) * height[j])
        return result

sol = Solution()
print sol.maximalRectangle_self(["10111", "01010", "11011", "11011", "01111"])
