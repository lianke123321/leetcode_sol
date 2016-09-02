# no Liana solution


import math


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        length, min_n, max_n = len(nums), float('inf'), -float('inf')
        for n in nums:
            min_n, max_n = min(min_n, n), max(max_n, n)
        if max_n - min_n < 2:
            return max_n - min_n

        gap = int(math.ceil(float(max_n - min_n) / (length - 1)))
        bucket_num = int(math.ceil(float(max_n - min_n) / gap))
        min_buckets = [float('inf')] * bucket_num
        max_buckets = [-float('inf')] * bucket_num
        for n in nums:
            if n == max_n or n == min_n:
                continue

            index = (n - min_n) / gap
            min_buckets[index] = min(min_buckets[index], n)
            max_buckets[index] = max(max_buckets[index], n)

        max_gap, prev = 0, min_n
        for i in xrange(bucket_num):
            if min_buckets[i] == float('inf') and max_buckets[i] == -float('inf'):
                continue
            max_gap = max(max_gap, min_buckets[i] - prev)
            prev = max_buckets[i]
        max_gap = max(max_gap, max_n - prev)
        return max_gap

sol = Solution()
print sol.maximumGap([1, 3, 4, 5, 8, 10])
