# no Liana solution


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res, i = 0, 0
        while i < len(nums) - 2:
            p1, p2 = i + 1, len(nums) - 1
            while p1 < p2:
                if nums[p1] + nums[p2] + nums[i] < target:
                    res += (p2 - p1)
                    p1 += 1
                else:
                    p2 -= 1
            i += 1
        return res

sol = Solution()
print sol.threeSumSmaller([-1, 1, -1, -1], -1)
