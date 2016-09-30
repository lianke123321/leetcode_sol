# no Liana solution


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        nums = [lower - 1] + nums + [upper + 1]
        for i in xrange(len(nums) - 1):
            if nums[i + 1] - nums[i] > 2:
                res.append(str(nums[i] + 1) + '->' + str(nums[i + 1] - 1))
            elif nums[i + 1] - nums[i] == 2:
                res.append(str(nums[i] + 1))
        return res

sol = Solution()
print sol.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
