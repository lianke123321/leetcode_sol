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
    def __init__(self):
        self.result = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.helper(nums, 0)
        return self.result

    def helper(self, nums, i):
        if i == len(nums) - 1:
            tmp = nums[:]
            self.result.append(tmp)
        else:
            for k in range(i, len(nums)):
                nums[k], nums[i] = nums[i], nums[k]
                self.helper(nums, i + 1)
                nums[k], nums[i] = nums[i], nums[k]

sol = Solution_self()
print sol.permute([1, 2, 3])
