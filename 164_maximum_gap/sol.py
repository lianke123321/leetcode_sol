# no Liana solution


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        # sort list first using radix sort
        self.radix_sort(nums)

        gap = 0
        for i in range(0, len(nums) - 1):
            if nums[i + 1] - nums[i] > gap:
                gap = nums[i + 1] - nums[i]
        return gap

    def radix_sort(self, nums):
        radix = 10
        placement = 1
        reach_max = False

        while not reach_max:
            reach_max = True
            buckets = [list() for _ in range(radix)]
            for num in nums:
                tmp = num / placement
                buckets[tmp % radix].append(num)
                if reach_max and tmp > 0:
                    reach_max = False

            p = 0
            for b in buckets:
                for num in b:
                    nums[p] = num
                    p += 1

            placement *= radix
