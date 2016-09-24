class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hashMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        res = ['']
        for i in range(0, len(digits)):
            while res and len(res[0]) == i:
                for c in hashMap[digits[i]]:
                    res += [res[0] + c]
                del res[0]
        return res

    def letterCombinations_self(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        num_to_letters = {'2': 'abc', '3': 'def', '4': 'ghi',
                          '5': 'jkl', '6': 'mno', '7': 'pqrs',
                          '8': 'tuv', '9': 'wxyz'}
        result = ['']
        if not digits:
            return result
        for i in xrange(len(digits)):
            while len(result[0]) == i:
                for letter in num_to_letters[digits[i]]:
                    result.append(result[0] + letter)
                del result[0]
        return result


class Solution_recursive(object):
    def __init__(self):
        self.num_to_letters = {'2': 'abc', '3': 'def', '4': 'ghi',
                               '5': 'jkl', '6': 'mno', '7': 'pqrs',
                               '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if not digits:
            return res
        self.helper('', digits, res)
        return res

    def helper(self, cache, digits, res):
        if not digits:
            res.append(cache)
        elif digits[0] in self.num_to_letters:
            for c in self.num_to_letters[digits[0]]:
                self.helper(cache + c, digits[1:], res)
