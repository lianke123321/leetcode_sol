# no Liana solution


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        targets = defaultdict(list)
        for i, j in sorted(tickets)[::-1]:
            targets[i].append(j)

        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack.append(targets[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]

sol = Solution()
print sol.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"],
                         ["ATL", "JFK"], ["ATL", "SFO"]])
