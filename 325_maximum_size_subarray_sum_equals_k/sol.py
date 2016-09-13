# no Liana solution


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap, max_len, total = {}, 0, 0
        for i in xrange(len(nums)):
            total += nums[i]
            if total == k:
                max_len = i + 1
            elif (total - k) in hashmap:
                max_len = max(max_len, i - hashmap[total - k])
            if total not in hashmap:
                hashmap[total] = i
        return max_len


sol = Solution()
print sol.maxSubArrayLen([-2, -1, 2, 1], 1)
