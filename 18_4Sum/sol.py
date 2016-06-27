class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(0, len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                newTarget = target - nums[i]
                for j in range(i + 1, len(nums) - 1):
                    if j == i + 1 or (j > i + 1 and nums[j] != nums[j - 1]):
                        lo = j + 1
                        hi = len(nums) - 1
                        sum = newTarget - nums[j]
                        while lo < hi:
                            if nums[lo] + nums[hi] == sum:
                                result.append([nums[i], nums[j], nums[lo], nums[hi]])
                                while lo < hi and nums[lo] == nums[lo + 1]:
                                    lo += 1
                                while lo < hi and nums[hi] == nums[hi - 1]:
                                    hi -= 1
                                lo += 1
                                hi -= 1
                            elif nums[lo] + nums[hi] < sum:
                                lo += 1
                            else:
                                hi -= 1
        return result

    def fourSum_self(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(0, len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                three_sum_target = target - nums[i]
                for j in range(i + 1, len(nums) - 2):
                    if j == i+1 or (nums[j] != nums[j-1]):
                        two_sum_target = three_sum_target - nums[j]
                        p1 = j + 1
                        p2 = len(nums) - 1
                        while p1 < p2:
                            if nums[p1] + nums[p2] == two_sum_target:
                                result.append([nums[i], nums[j], nums[p1], nums[p2]])
                                while p1 < p2 and nums[p1] == nums[p1 + 1]:
                                    p1 += 1
                                while p1 < p2 and nums[p2] == nums[p2 - 1]:
                                    p2 -= 1
                                p1 += 1
                                p2 -= 1
                            elif nums[p1] + nums[p2] < two_sum_target:
                                p1 += 1
                            else:
                                p2 -= 1
        return result

sol = Solution()
print sol.fourSum_self([1, 0, -1, 0, -2, 2], 0)
