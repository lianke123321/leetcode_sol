# no Liana solution


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.find_words(s, 0, wordDict, {})

    def find_words(self, s, start, wordDict, cache):
        # here we prune a lot of branches
        if start in cache:
            return cache[start]
        cache[start], candidate, current = [], '', start
        while current < len(s):
            candidate += s[current]
            current += 1
            if candidate in wordDict:
                if current == len(s):
                    cache[start].append(candidate)
                else:
                    for x in self.find_words(s, current, wordDict, cache):
                        cache[start].append(candidate + ' ' + x)
        return cache[start]

sol = Solution()
print sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
