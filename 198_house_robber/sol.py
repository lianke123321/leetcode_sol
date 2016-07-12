# no Liana solution


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        count = len(nums)
        result = [0 for _ in range(count + 1)]
        result[0] = 0
        result[1] = nums[0]

        for i in range(2, count + 1):
            result[i] = max(result[i - 1], result[i - 2] + nums[i - 1])
        return result[count]
