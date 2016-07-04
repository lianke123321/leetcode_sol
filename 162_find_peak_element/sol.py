class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid1 = lo + (hi - lo) / 2
            mid2 = mid1 + 1
            if nums[mid2] > nums[mid1]:
                lo = mid2
            else:
                hi = mid1
        return lo

    def findPeakElement_self(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid1 = lo + (hi - lo) / 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                lo = mid2
            else:
                hi = mid1
        return lo
