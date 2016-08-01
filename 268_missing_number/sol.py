class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use bit manipulation
        result = len(nums)
        i = 0
        for n in nums:
            result ^= n
            result ^= i
            i += 1
        return result

    def missingNumber_self(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)

    def missingNumber_self_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        i = 1
        for n in nums:
            result ^= n
            result ^= i
            i += 1
        return result

sol = Solution()
print sol.missingNumber([0, 3, 1])
