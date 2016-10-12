# no Liana solution


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        n, remainder = divmod(numerator, denominator)
        res = [sign + str(n), '.']
        cache = []
        while remainder not in cache:
            cache.append(remainder)
            n, remainder = divmod(remainder * 10, denominator)
            res.append(str(n))

        idx = cache.index(remainder)
        res.insert(idx + 2, '(')
        res.append(')')
        return ''.join(res).replace('(0)', '').rstrip('.')

sol = Solution()
print sol.fractionToDecimal(3, 11)
