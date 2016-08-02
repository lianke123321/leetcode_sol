# no Liana solution


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        nums = [-1] * n
        for edge in edges:
            x = self.find(nums, edge[0])
            y = self.find(nums, edge[1])

            if x == y:
                return False

            nums[x] = y

        return len(edges) == n - 1

    def find(self, nums, i):
        if nums[i] == -1:
            return i
        return self.find(nums, nums[i])
