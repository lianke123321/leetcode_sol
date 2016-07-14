class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # store the result that is the max we have found so far
        result = nums[0]
        # imax/imin stores the max/min product of
        # subarray that ends with the current number nums[i]
        imax = result
        imin = result
        for i in range(1, len(nums)):
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if nums[i] < 0:
                imax, imin = imin, imax
            # max/min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])
            # the newly computed max value is a candidate for our global result
            result = max(result, imax)
        return result

    def maxProduct_self(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        max_so_far, min_end_here, max_end_here = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                min_end_here, max_end_here = max_end_here, min_end_here
            max_end_here = max(max_end_here * nums[i], nums[i])
            min_end_here = min(min_end_here * nums[i], nums[i])
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far
