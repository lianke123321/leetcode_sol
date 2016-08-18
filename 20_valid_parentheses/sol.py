class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {']': '[', '}': '{', ')': '('}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

    def isValid_self(self, s):
        """
        :type s: str
        :rtype: bool
        """
        right_to_left = {']': '[',
                         '}': '{',
                         ')': '('}
        stack = []
        for char in s:
            if char in right_to_left:
                if len(stack) == 0 or right_to_left[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return stack == []

sol = Solution()
print sol.isValid_self('()')
