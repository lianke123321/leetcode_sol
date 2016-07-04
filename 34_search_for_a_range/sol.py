class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            if nums[lo] == nums[hi] == target:
                return [lo, hi]
            if nums[lo] < target:
                lo += 1
            if nums[hi] > target:
                hi -= 1
        return [-1, -1]

    def searchRange_self(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        low = 0
        high = len(nums) - 1
        while low != high:
            mid = (low + high) / 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1

        if nums[low] != target:
            return [-1, -1]

        while high < len(nums) and nums[high] == target:
            high += 1

        return [low, high - 1]

test_nums = [1]
sol = Solution()
print sol.searchRange_self(test_nums, 1)