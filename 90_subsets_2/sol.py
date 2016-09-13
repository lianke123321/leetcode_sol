class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        nums.sort() #sort the array to avoid descending list of int
        res = [[]]
        for element in nums:
            temp = []
            for ans in res:
                 #append the new int to each existing list
                if ans + [element] not in res:
                    temp.append(ans + [element])
            res += temp
        return res

    def subsetsWithDup_self(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        if not nums:
            return res
        nums.sort()
        dup = len(res)
        for i in xrange(len(nums)):
            if i > 0 and nums[i] != nums[i - 1]:
                dup = len(res)
            for j in xrange(len(res) - dup, len(res)):
                res.append(res[j] + [nums[i]])
        return res

sol = Solution()
print sol.subsetsWithDup_self([5, 5, 5, 5, 5])
