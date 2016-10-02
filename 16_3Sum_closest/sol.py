class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        for i in range(0, len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                lo = i + 1
                hi = len(nums) - 1
                while lo < hi:
                    sum = nums[i] + nums[lo] + nums[hi]
                    if sum < target:
                        lo += 1
                    else:
                        hi -= 1
                    if abs(sum - target) < abs(result - target):
                        result = sum
        return result

    def threeSumClosest_self(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        # initialize result to be positive infinite
        result = nums[0] + nums[1] + nums[-1]
        for i in xrange(0, len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                p1 = i + 1
                p2 = len(nums) - 1
                while p1 < p2:
                    sum = nums[i] + nums[p1] + nums[p2]
                    if sum < target:
                        p1 += 1
                    else:
                        p2 -= 1
                    if abs(target - sum) < abs(target - result):
                        result = sum
                        if result == target:
                            return result
        return result

sol = Solution()
print sol.threeSumClosest_self([-1, 2, 1, -4], 1)
