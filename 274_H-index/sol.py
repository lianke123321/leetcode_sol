class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        length = len(citations)
        h = 0
        count = [0 for i in range(length + 1)]
        for c in citations:
            count[min(c, length)] += 1
        for i in range(length + 1):
            h += count[length - i]
            if h >= length - i:
                return length - i

    def hIndex_self(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        if length == 0:
            return 0

        tmp = [0] * (length + 1)

        for c in citations:
            if c > length:
                tmp[-1] += 1
            else:
                tmp[c] += 1

        h = 0
        for i in reversed(xrange(length + 1)):
            h += tmp[i]
            if h >= i:
                return i

sol = Solution()
print sol.hIndex_self([1, 2])
