# no Liana solution


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        if count == 0:
            return 0
        elif count == 1:
            return nums[0]
        elif count == 2:
            return max(nums[0], nums[1])

        # max income to rob first n-1 houses
        dp = [0 for _ in range(count)]
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, count):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        max_1 = dp[count - 1]

        # max income to rob last n-1 houses
        dp[0] = 0
        dp[1] = nums[1]
        for i in range(2, count):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return max(max_1, dp[count - 1])
