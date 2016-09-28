from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.index = -1
        self.palindrome = []


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        root = self.build_reverse_trie(words)
        palindrome_cache = [[] for _ in xrange(len(words))]
        for i in xrange(len(words)):
            for j in xrange(len(words[i])):
                palindrome_cache[i].append(self.isPalindrome(words[i][j:]))

        result = []
        for i in xrange(len(words)):
            current = root
            for j in xrange(len(words[i])):
                if current.index >= 0 and current.index != i and palindrome_cache[i][j]:
                    result.append([i, current.index])
                current = current.children.get(words[i][j])
                if not current:
                    break
            # go through all partial palindrome words at this node
            if current:
                for j in current.palindrome:
                    if i != j:
                        result.append([i, j])
        return result

    def build_reverse_trie(self, words):
        root = TrieNode()
        for i in xrange(len(words)):
            current = root
            for j in reversed(xrange(len(words[i]))):
                if self.isPalindrome(words[i][:j + 1]):
                    current.palindrome.append(i)
                current = current.children[words[i][j]]
            current.index = i
            current.palindrome.append(i)
        return root

    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
