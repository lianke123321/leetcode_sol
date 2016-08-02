# no Liana solution
from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = self.build_trie(words)
        result = []
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j, root, result)
        return result

    def build_trie(self, words):
        root = TrieNode()
        for w in words:
            current = root
            for letter in w:
                current = current.children[letter]
            current.word = w
        return root

    def dfs(self, board, i, j, current, result):
        c = board[i][j]
        if c == '#' or not current.children.get(c):
            return
        current = current.children[c]
        if current.word:
            result.append(current.word)
            current.word = None

        board[i][j] = '#'
        if i > 0: self.dfs(board, i - 1, j, current, result)
        if j > 0: self.dfs(board, i, j - 1, current, result)
        if i < len(board) - 1: self.dfs(board, i + 1, j, current, result)
        if j < len(board[0]) - 1: self.dfs(board, i, j + 1, current, result)
        board[i][j] = c

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
sol = Solution()
print sol.findWords(board, ["oath", "pea", "eat", "rain"])
