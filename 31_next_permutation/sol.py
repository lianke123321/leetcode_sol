class Solution(object):
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:  # nums are in descending order
            self.reverse(nums, 0, len(nums) - 1)
            return
        k = i - 1  # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        """
        l, r = k + 1, len(nums) - 1  # reverse the second part
        while l < r:
        	nums[l], nums[r] = nums[r], nums[l]
        	l += 1 ; r -= 1
        """
        self.reverse(nums, k + 1, len(nums) - 1)


class Solution_self(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()  # same as self.reverse_list(nums, 0, len(nums) - 1) but is faster
            return

        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        self.reverse_list(nums, i, len(nums) - 1)

    def reverse_list(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
