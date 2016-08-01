class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                major = nums[i]
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major

    def majorityElement_self(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, count = nums[0], 1
        for i in xrange(1, len(nums)):
            if count == 0:
                result = nums[i]
                count += 1
            elif result == nums[i]:
                count += 1
            else:
                count -= 1
        return result
