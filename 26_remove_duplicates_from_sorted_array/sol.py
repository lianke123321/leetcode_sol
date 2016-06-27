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
            if n != nums[newTail]:
                nums[newTail + 1] = n
                newTail += 1
        return newTail + 1

    def removeDuplicates_self(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_len = 0
        if len(nums) == 0:
            return new_len
        for n in nums:
            if n != nums[new_len]:
                nums[new_len + 1] = n
                new_len += 1
        return new_len + 1