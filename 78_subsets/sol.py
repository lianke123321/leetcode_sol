class Solution:
    def subsets(self, nums):
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
                temp.append(ans + [element])
            res += temp
        return res

    def subsets_self(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        if not nums:
            return result
        for n in nums:
            for j in xrange(len(result)):
                result.append(result[j] + [n])
        return result

sol = Solution()
print sol.subsets_self([1,4,3])
