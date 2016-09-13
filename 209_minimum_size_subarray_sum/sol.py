class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        firstPos = 0
        numberSum = 0
        INT_MAX = 2147483647
        minLength = INT_MAX
        for i in range(len(nums)):
            numberSum += nums[i]
            while numberSum >= s:
                minLength = min(minLength, i - firstPos + 1)
                numberSum -= nums[firstPos]
                firstPos += 1
        if minLength == INT_MAX:
            return 0
        else:
            return minLength

    def minSubArrayLen_self(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start, end, res, total = 0, 0, float('inf'), 0
        while end < len(nums):
            while total < s and end < len(nums):
                total += nums[end]
                end += 1
            while total >= s and start < end:
                res = min(res, end - start)
                total -= nums[start]
                start += 1
        return res if res < float('inf') else 0

sol = Solution()
print sol.minSubArrayLen_self(7, [2,3,1,2,4,3])
