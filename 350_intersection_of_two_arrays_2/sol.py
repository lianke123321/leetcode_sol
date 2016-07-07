# no Liana solution


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c1, c2 = Counter(nums1), Counter(nums2)
        result = []
        for num in c1 & c2:
            result.extend([num] * min(c1[num], c2[num]))
        return result


sol = Solution()
print sol.intersect([2, 3, 444, 5, 6], [3, 3, 6, 6])
