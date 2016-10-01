# no Liana solution


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return nums
        nums.sort()
        dp = [[nums[0]]] + [[]] * (len(nums) - 1)
        res = dp[0]

        for i in xrange(1, len(dp)):
            tmp = []
            for j in xrange(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) > len(tmp):
                    tmp = dp[j]
            dp[i] = tmp + [nums[i]]
            if len(dp[i]) > len(res):
                res = dp[i]
        return res


sol = Solution()
print sol.largestDivisibleSubset([3, 4, 16, 8])
