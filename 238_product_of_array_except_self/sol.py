class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0 for n in nums]
        temp = 1
        length = len(nums)
        for i in range(length):
            result[i] = temp
            temp *= nums[i]
        temp = 1
        for i in range(length):
            result[length - i - 1] *= temp
            temp *= nums[length - i - 1]
        return result

    def productExceptSelf_self(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, tmp = [0] * len(nums), 1
        for i in xrange(len(nums)):
            res[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for i in reversed(xrange(len(nums))):
            res[i] *= tmp
            tmp *= nums[i]
        return res

sol = Solution()
print sol.productExceptSelf_self([1, 2, 3, 4])
