class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        high = len(nums) - 1
        low = 0

        for i in range(low, high):
            while nums[i] == max(nums) and i < high:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            while nums[i] == 0 and i > low:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1

    def sortColors_self(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_idx, idx, two_idx = 0, 0, len(nums) - 1
        while idx <= two_idx and zero_idx < two_idx:
            if nums[idx] == 0:
                nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
                zero_idx += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx], nums[two_idx] = nums[two_idx], nums[idx]
                two_idx -= 1
            else:
                idx += 1
