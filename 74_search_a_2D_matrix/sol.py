class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

    def searchMatrix_self(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l1 = 0
        h1 = len(matrix) - 1
        while l1 <= h1:
            if target < matrix[l1][0] or target > matrix[h1][-1]:
                return False

            if l1 < h1:
                m1 = (l1 + h1) / 2
                if target > matrix[m1][0]:
                    if target > matrix[m1][-1]:
                        l1 = m1 + 1
                    else:
                        l1 = h1 = m1
                elif target < matrix[m1][0]:
                    h1 = m1 - 1
                else:
                    return True
            else:
                l2 = 0
                h2 = len(matrix[l1]) - 1
                while l2 <= h2:
                    m2 = (l2 + h2) / 2
                    if matrix[l1][m2] > target:
                        h2 = m2 - 1
                    elif matrix[l1][m2] < target:
                        l2 = m2 + 1
                    else:
                        return True
                break

        return False

sol = Solution()
print sol.searchMatrix_self([[1]], 1)
