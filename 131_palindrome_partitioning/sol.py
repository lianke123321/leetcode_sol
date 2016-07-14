class Solution:
    def isPalindromic(self, s):
        result = True
        length = len(s)
        for i in range(length / 2):
            if s[i] != s[length - 1 - i]:
                result = False
                break
        return result

    def backTracking(self, s, result, stack):
        for i in range(0, len(s) + 1):
            if i == 0:
                continue
            if self.isPalindromic(s[0: i]):
                #print s
                #print i
                stack.append(s[0: i])
                if i != len(s):
                    new_s = s[i: len(s)]
                    self.backTracking(new_s, result, stack)
                else:
                    result.append(stack[:])
                    #print "s = %s, i = %s" % (s, i)
                    #print stack
                    if stack:
                        stack.pop()
        if stack:
            stack.pop()
        return result

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        stack = []
        return self.backTracking(s, result, stack)


class Solution_self(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return self.backtracking(s, [], [])

    def backtracking(self, s, stack, result):
        for i in xrange(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                stack.append(s[:i])
                if i != len(s):
                    self.backtracking(s[i:], stack, result)
                else:
                    result.append(stack[:])
                    if stack:
                        stack.pop()
        if stack:
            stack.pop()
        return result

    def isPalindrome(self, s):
        if len(s) < 2:
            return True
        else:
            return s[:len(s) / 2] == s[-1:len(s) / 2 + len(s) % 2 - 1:-1]

sol = Solution_self()
print sol.partition('abcdcba')
