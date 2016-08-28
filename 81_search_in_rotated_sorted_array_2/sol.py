class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) / 2
            if target == nums[mid]:
                return True
            # tricky part
            while low < mid and nums[low] == nums[mid]:
                low += 1
            # the first half is ordered
            if nums[low] <= nums[mid]:
                # target is in the first half
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

    def search_self(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if nums[mid] == target:
                return True
            elif lo == hi:
                return False

            if nums[mid] > nums[hi]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] < nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                hi -= 1
        return False
