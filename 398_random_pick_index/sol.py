# no Liana solution


from random import randint


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res, total = None, 0
        for i in xrange(len(self.nums)):
            if self.nums[i] == target:
                total += 1
                if randint(1, total) == total:
                    res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
