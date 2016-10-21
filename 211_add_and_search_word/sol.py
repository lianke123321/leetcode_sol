# skipped Liana solution


from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word, current=None):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :type current: TrieNode
        :rtype: bool
        """
        current = current or self.root
        for i in xrange(len(word)):
            if word[i] == '.':
                tmp = current
                for k in tmp.children:
                    current = tmp.children.get(k)
                    if self.search(word[i + 1:], current):
                        return True
                return False
            else:
                current = current.children.get(word[i])
                if not current:
                    return False
        return current.is_word

wd = WordDictionary()
wd.addWord('bad')
wd.addWord('dad')
wd.addWord('mad')
print wd.search('pad')
print wd.search('bad')
print wd.search('.ad')
print wd.search('b..')
