# no Liana solution


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)

        def mergesort(enums):
            mid = len(enums) / 2
            if mid:
                left, right = mergesort(enums[:mid]), mergesort(enums[mid:])
                for i in reversed(xrange(len(enums))):
                    if not right or (left and left[-1][1] > right[-1][1]):
                        result[left[-1][0]] += len(right)
                        enums[i] = left.pop()
                    else:
                        enums[i] = right.pop()
            return enums

        mergesort(list(enumerate(nums)))
        return result

sol = Solution()
print sol.countSmaller([5, 2, 6, 1])
