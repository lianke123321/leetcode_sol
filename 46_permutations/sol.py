class Solution:
    def recursion(self, nums, i, n, result):
        if i == n - 1:
            temp = []
            for k in range(0, n):
                temp.append(nums[k])
            result.append(temp)
        else:
            for k in range(i, n):
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = temp
                self.recursion(nums, i + 1, n, result)
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = temp

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.recursion(nums, 0, len(nums), result)
        return result


class Solution_self(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.recursion(nums, 0, len(nums), result)
        return result

    def recursion(self, nums, i, n, result):
        if i == n - 1:
            result.append(nums[:])
        else:
            for k in xrange(i, n):
                nums[i], nums[k] = nums[k], nums[i]
                self.recursion(nums, i + 1, n, result)
                nums[i], nums[k] = nums[k], nums[i]

sol = Solution_self()
print sol.permute([1, 2, 3])
