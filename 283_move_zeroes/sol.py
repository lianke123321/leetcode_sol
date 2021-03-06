class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 0
        while end < len(nums) - 1:
            if nums[end] == 0:
                if nums[end + 1] != 0:
                    temp = start
                    nums[start], nums[end + 1] = nums[end + 1], nums[start]
                    start = temp + 1
            else:
                start += 1
            end += 1

    def moveZeroes_self(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, p = 0, 0
        while p < len(nums) - 1:
            while start < len(nums) and nums[start] != 0:
                start += 1
            p = max(p, start)
            while p < len(nums) and nums[p] == 0:
                p += 1
            if p < len(nums):
                nums[start], nums[p] = nums[p], nums[start]

nums = [1, 0, 3, 2, 0]
sol = Solution()
sol.moveZeroes_self(nums)
print nums
