class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not (len(nums) == len(set(nums)))

    def containsDuplicate_self(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(nums) == len(set(nums))
