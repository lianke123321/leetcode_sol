# no Liana solution


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict
        graph = defaultdict(list)
        chars = set(''.join(words))
        degree = {x: 0 for x in chars}
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    graph[a].append(b)
                    degree[b] += 1
                    break

        stack = [x for x in degree if degree[x] == 0]
        result = ''
        while stack:
            x = stack.pop()
            result += x
            for i in graph[x]:
                degree[i] -= 1
                if degree[i] == 0:
                    stack.append(i)
        return result if len(result) == len(chars) else ''


sol = Solution()
print sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
