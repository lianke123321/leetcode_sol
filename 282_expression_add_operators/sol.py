# no Liana solution


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result = []
        for i in xrange(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.helper(target, num[i:], num[:i], int(num[:i]), int(num[:i]), result)
        return result

    def helper(self, target, num, tmp, curr, last, result):
        if not num:
            if curr == target:
                result.append(tmp)
        for i in xrange(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.helper(target, num[i:], tmp + '+' + num[:i], curr + int(num[:i]), int(num[:i]), result)
                self.helper(target, num[i:], tmp + '-' + num[:i], curr - int(num[:i]), -int(num[:i]), result)
                self.helper(target, num[i:], tmp + '*' + num[:i], curr - last + last * int(num[:i]),
                            last * int(num[:i]), result)

sol = Solution()
print sol.addOperators('232', 8)
