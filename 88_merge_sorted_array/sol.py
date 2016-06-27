class Solution:
    def merge(self, nums1, m, nums2, n):
        """
            :type nums1: List[int]
            :type m: int
            :type nums2: List[int]
            :type n: int
            :rtype: void Do not return anything, modify nums1 in-place instead.
            """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[: n] = nums2[: n]
        #print nums1

    def merge_self(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:n] = nums2[:n]
            return

        result = [0] * (m + n)

        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                result[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                result[m + n - 1] = nums2[n - 1]
                n -= 1

        if m > 0:
            result[:m] = nums1[:m]
        if n > 0:
            result[:n] = nums2[:n]

        nums1[:len(result)] = result[:len(result)]
        return

sol = Solution()
nums1 = [0]
sol.merge_self(nums1, 0, [1], 1)
print nums1
