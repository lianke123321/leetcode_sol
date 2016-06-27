class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(0, len(nums) - 1):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                lo = i + 1
                hi = len(nums) - 1
                sum = 0 - nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == sum:
                        result.append([nums[i], nums[lo], nums[hi]])
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

    def threeSum_self(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(0, len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                p1 = i + 1
                p2 = len(nums) - 1
                wanted = 0 - nums[i]
                while p1 < p2:
                    if nums[p1] + nums[p2] == wanted:
                        result.append([nums[i], nums[p1], nums[p2]])
                        while p1 < p2 and nums[p1] == nums[p1 + 1]:
                            p1 += 1
                        while p1 < p2 and nums[p2] == nums[p2 - 1]:
                            p2 -= 1
                        p1 += 1
                        p2 -= 1
                    elif nums[p1] + nums[p2] < wanted:
                        p1 += 1
                    else:
                        p2 -= 1
        return result

sol = Solution()
print sol.threeSum_self([-1, 0, 1, 2, -1, -4])
