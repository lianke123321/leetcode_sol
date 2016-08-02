# no Liana solution


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        nums = [-1] * n
        result = n
        for i, j in edges:
            x = self.find(nums, i)
            y = self.find(nums, j)

            if x != y:
                nums[x] = y
                result -= 1
        return result

    def find(self, nums, i):
        if nums[i] == -1:
            return i
        return self.find(nums, nums[i])

sol = Solution()
print sol.countComponents(5, [[0, 1], [1, 2], [3, 4]])
