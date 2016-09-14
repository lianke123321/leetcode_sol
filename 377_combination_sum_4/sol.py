# no Liana solution


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [0] * (target + 1)
        for i in xrange(1, target + 1):
            for n in nums:
                if n > i:
                    break
                elif n == i:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - n]
        return dp[-1]
