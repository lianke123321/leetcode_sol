# no Liana solution


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        rword_to_index, result = {word[::-1]: i for i, word in enumerate(words)}, []
        for i, word in enumerate(words):
            for j in xrange(len(word) + 1):
                prefix, postfix = word[:j], word[j:]
                if prefix in rword_to_index and rword_to_index[prefix] != i and postfix == postfix[::-1]:
                    result.append([i, rword_to_index[prefix]])
                if j > 0 and postfix in rword_to_index and i != rword_to_index[postfix] and prefix == prefix[::-1]:
                    result.append([rword_to_index[postfix], i])
        return result

sol = Solution()
print sol.palindromePairs(["abcd","dcba","lls","s","sssll"])
