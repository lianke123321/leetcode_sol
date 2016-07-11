class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        hashMap1 = {}
        hashMap2 = {}
        str = str.split()
        if len(pattern) != len(str):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in hashMap1:
                hashMap1[pattern[i]] = str[i]
            elif hashMap1[pattern[i]] != str[i]:
                return False
        for key in hashMap1:
            if hashMap1[key] not in hashMap2:
                hashMap2[hashMap1[key]] = key
            elif hashMap2[hashMap1[key]] != key:
                return False
        return True

    def wordPattern_self(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        hashmap = {}
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                hashmap[pattern[i]] = words[i]
            elif hashmap[pattern[i]] != words[i]:
                return False

        hashmap = {}
        for i in range(len(words)):
            if words[i] not in hashmap:
                hashmap[words[i]] = pattern[i]
            elif hashmap[words[i]] != pattern[i]:
                return False

        print hashmap
        return True

sol = Solution()
print sol.wordPattern_self("abba", "dog dog dog dog")
