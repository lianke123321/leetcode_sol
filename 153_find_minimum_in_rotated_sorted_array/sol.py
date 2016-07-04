class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            if nums[lo] < nums[hi]:
                return nums[lo]
            mid = lo + (hi - lo) / 2
            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

    def findMin_self(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = nums[0]

        if first < nums[-1]:
            return first

        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] >= first:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]
