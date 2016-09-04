# no Liana solution


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        max_size = 0
        for n in nums:
            start, end = 0, max_size
            while start < end:
                mid = (start + end) >> 1
                if tails[mid] < n:
                    start = mid + 1
                else:
                    end = mid
            tails[start] = n
            max_size = max(max_size, start + 1)
        return max_size

sol = Solution()
print sol.lengthOfLIS([10,9,2,5,3,7,101,18])
