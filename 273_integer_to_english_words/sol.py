class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousands = 'Thousand Million Billion'.split()

        def words(n):
            if n < 20:
                return to19[n - 1: n]
            if n < 100:
                return [tens[n / 10 - 2]] + words(n % 10)
            if n < 1000:
                return [to19[n / 100 - 1]] + ['Hundred'] + words(n % 100)
                # for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
            for p in range(1, 4):
                if n < 1000 ** (p + 1):
                    return words(n / 1000 ** p) + [thousands[p - 1]] + words(n % 1000 ** p)

        return ' '.join(words(num)) or 'Zero'

    def numberToWords_self(self, num):
        """
        :type num: int
        :rtype: str
        """
        one_to_19 = 'One,Two,Three,Four,Five,Six,Seven,Eight,Nine,Ten,Eleven,Twelve,' \
                    'Thirteen,Fourteen,Fifteen,Sixteen,Seventeen,Eighteen,Nineteen'.split(',')
        tens = 'Twenty,Thirty,Forty,Fifty,Sixty,Seventy,Eighty,Ninety'.split(',')
        thousands = 'Thousand,Million,Billion'.split(',')

        def convert_words(n):
            if n == 0:
                return []
            if n < 20:
                return [one_to_19[n - 1]]
            elif n < 100:
                return [tens[n / 10 - 2]] + convert_words(n % 10)
            elif n < 1000:
                return [one_to_19[n / 100 - 1]] + ['Hundred'] + convert_words(n % 100)
            for p in xrange(2, 5):
                if n < 1000 ** p:
                    return convert_words(n / 1000 ** (p - 1))\
                           + [thousands[p - 2]] + convert_words(n % 1000 ** (p - 1))

        return ' '.join(convert_words(num)) if num else 'Zero'


sol = Solution()
print sol.numberToWords_self(20)
