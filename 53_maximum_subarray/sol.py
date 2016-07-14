class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length > 0:
            maxSoFar = nums[0]
            maxEndingHere = nums[0]
            for i in range(1, length):
                maxEndingHere = max(maxEndingHere + nums[i], nums[i])
                maxSoFar = max(maxSoFar, maxEndingHere)
            return maxSoFar
        else:
            return 0

    def maxSubArray_self(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        if count == 0:
            return 0

        max_so_far, max_ending_here = nums[0], nums[0]
        for i in xrange(1, count):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
