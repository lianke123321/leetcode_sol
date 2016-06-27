class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        newTail = 0
        for n in nums:
            if newTail < 2 or n > nums[newTail - 2]:
                nums[newTail] = n
                newTail += 1
        return newTail

    def removeDuplicates_self(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_len = 0
        if len(nums) == 0:
            return new_len
        for n in nums:
            if new_len <= 1 or n != nums[new_len - 2]:
                nums[new_len] = n
                new_len += 1
        return new_len

sol = Solution()
test = [1, 1, 1, 1]
print sol.removeDuplicates_self(test)
print test
