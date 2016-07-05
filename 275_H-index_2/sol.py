class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        lo = 0
        hi = length - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if citations[mid] == length - mid:
                return citations[mid]
                # if citations[mid] < length - mid:
            elif citations[mid] < length - mid:
                lo = mid + 1
            else:
                hi = mid - 1
        # return length - lo
        return length - (hi + 1)

    def hIndex_self(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        num_of_papers = len(citations)
        lo = 0
        hi = num_of_papers - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if num_of_papers - mid == citations[mid]:
                return citations[mid]
            elif num_of_papers - mid > citations[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        # in this case, num of citations is more than number of
        # papers that has this num of citations, so set h to be
        # the num of papers instead of num of citations
        return num_of_papers - (hi + 1)

sol  = Solution()
print sol.hIndex_self([100])
