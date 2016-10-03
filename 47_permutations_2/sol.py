class Solution:
    def duplicated(self, nums, i, j):
        for t in range(i, j):
            if nums[t] == nums[j]:
                return False
        return True

    def recursion(self, nums, i, n, result):
        if i == n - 1:
            temp = []
            for k in range(0, n):
                temp.append(nums[k])
            result.append(temp)
        else:
            for k in range(i, n):
                if self.duplicated(nums, i ,k):
                    temp = nums[k] #swap
                    nums[k] = nums[i]
                    nums[i] = temp

                    self.recursion(nums, i + 1, n, result)

                    temp = nums[k] #swap
                    nums[k] = nums[i]
                    nums[i] = temp

    def permuteUnique(self, nums):
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

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.helper(nums, 0)
        return self.result

    def helper(self, nums, i):
        if i == len(nums) - 1:
            self.result.append(nums[:])
        else:
            appeared_nums = set()
            for k in range(i, len(nums)):
                if nums[k] not in appeared_nums:
                    nums[k], nums[i] = nums[i], nums[k]
                    self.helper(nums, i + 1)
                    nums[k], nums[i] = nums[i], nums[k]
                    appeared_nums.add(nums[k])

sol = Solution_self()
print sol.permuteUnique([2, 2, 1, 1])
