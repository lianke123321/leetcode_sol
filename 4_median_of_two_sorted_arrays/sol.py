class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if j > 0 and i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and j < n and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    n1 = nums2[j - 1]
                elif j == 0:
                    n1 = nums1[i - 1]
                else:
                    n1 = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return n1
                if i == m:
                    n2 = nums2[j]
                elif j == n:
                    n2 = nums1[i]
                else:
                    n2 = min(nums1[i], nums2[j])
                return (n1 + n2) / 2.0

    def findMedianSortedArrays_self(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)

        # always make sure that m is smaller
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        # half_len will be the bigger half if m + n is odd
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while True:
            # i is from 0 to m, and j is from 0 to n, so the
            # boundry is between i-1 and i (j-1 and j), so i
            # and j could be pointing to the index behind the
            # last item in nums1 and nums2
            i = (imin + imax) / 2
            # because of how we calculate j, i + j = half_len
            # means that the sum of left parts of nums1 and
            # nums2 will be bigger part if m + n is odd
            j = half_len - i
            if j > 0 and i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1
            elif i > 0 and j < n and nums2[j] < nums1[i - 1]:
                imax = i - 1
            else:
                if i == 0:
                    n1 = nums2[j - 1]
                elif j == 0:
                    n1 = nums1[i - 1]
                else:
                    n1 = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return n1

                if i == m:
                    n2 = nums2[j]
                elif j == n:
                    n2 = nums1[i]
                else:
                    n2 = min(nums1[i], nums2[j])

                return (n1 + n2) / 2.0
