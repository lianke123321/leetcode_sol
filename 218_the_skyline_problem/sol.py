# no Liana solution


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from heapq import heappush, heappop
        result = [[-1, 0]]
        pos = sorted(list(set([b[0] for b in buildings] + [b[1] for b in buildings])))
        live_heap = []
        i = 0

        for p in pos:
            while i < len(buildings) and buildings[i][0] <= p:
                heappush(live_heap, (-buildings[i][2], buildings[i][1]))
                i += 1

            while live_heap and live_heap[0][1] <= p:
                heappop(live_heap)

            h = -live_heap[0][0] if live_heap else 0
            if result[-1][1] != h:
                result.append([p, h])

        return result[1:]

sol = Solution()
print sol.getSkyline([[0, 1, 3]])
