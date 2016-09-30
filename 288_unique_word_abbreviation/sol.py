# no Liana solution


from collections import defaultdict


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrs = defaultdict(set)
        for word in dictionary:
            if len(word) > 2:
                abbr = word[0] + str(len(word[1:-1])) + word[-1]
                self.abbrs[abbr].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) > 2:
            abbr = word[0] + str(len(word[1:-1])) + word[-1]
            if abbr not in self.abbrs or (len(self.abbrs[abbr]) == 1 and word in self.abbrs[abbr]):
                return True
            return False
        else:
            return True


# Your ValidWordAbbr object will be instantiated and called as such:
vwa = ValidWordAbbr(["hello", "cat"])
print vwa.isUnique("hello")
print vwa.isUnique("hello")
