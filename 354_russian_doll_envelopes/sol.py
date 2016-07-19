# no Liana solution


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        import bisect
        doll_heights = [None] * len(envelopes)
        end = 0
        for _, h in sorted(envelopes, key=lambda (w, h): (w, -h)):
            i = bisect.bisect_left(doll_heights, h, hi=end)
            doll_heights[i] = h
            end += i == end
        return end

sol = Solution()
print sol.maxEnvelopes([[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]])
