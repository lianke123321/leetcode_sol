class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i + 1
            else:
                return map[nums[i]], i + 1

        return -1, -1

    def twoSum_self(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        value_to_index = {}
        for i in range(len(nums)):
            if nums[i] not in value_to_index:
                value_to_index[target - nums[i]] = i
            else:
                return [value_to_index[nums[i]], i]

        return [-1, -1]

sol = Solution()
print sol.twoSum_self([2, 7, 11, 15], 9)
