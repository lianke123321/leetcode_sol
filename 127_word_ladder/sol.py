class Solution:
    def ladderLength(self, beginWord, endWord, wordDict):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        stack = []
        stack.append([beginWord, 1])

        while(stack):
            w = stack[0][0]
            d = stack[0][1]
            for i in range(len(w)):
                temp1 = w[0: i]
                temp2 = w[i + 1:]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    word = temp1 + c + temp2
                    if c == w[i]:
                        continue
                    if word == endWord:
                        return d + 1
                    if word in wordDict:
                        stack.append([word, d + 1])
                        wordDict.remove(word)
            del stack[0]
            #print stack
            #print "stack = %s" % stack
        return 0

    def ladderLength_self(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        start, end, length = {beginWord}, {endWord}, 2
        wordList -= start
        while start:
            start = wordList & set([word[:i] + char + word[i + 1:] for word in start
                                    for i in xrange(len(word)) for char in 'abcdefghijklmnopqrstuvwxyz'])
            if start & end:
                return length
            length += 1
            if len(start) > len(end):
                start, end = end, start
            wordList -= start
        return 0

sol = Solution()
print sol.ladderLength_self('a', 'c', {'a', 'b', 'c'})
