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
        counter = [0] * 3
        for num in nums:
            counter[num] += 1

        p = 0
        for i in range(len(counter)):
            while counter[i] > 0:
                nums[p] = i
                p += 1
                counter[i] -= 1
