class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            result = nums[0]
            for i in range(1, len(nums)):
                result ^= nums[i]
            return result
        else:
            return 0

    def singleNumber_self(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for n in nums:
            result ^= n
        return result
