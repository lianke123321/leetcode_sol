# no Liana solution


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull_count = 0
        cow_count = 0
        hashmap_secret = {}
        hashmap_guess = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull_count += 1
            else:
                if secret[i] not in hashmap_secret:
                    hashmap_secret[secret[i]] = 1
                else:
                    hashmap_secret[secret[i]] += 1

                if guess[i] not in hashmap_guess:
                    hashmap_guess[guess[i]] = 1
                else:
                    hashmap_guess[guess[i]] += 1

        for k in hashmap_secret:
            if k in hashmap_guess:
                cow_count += min(hashmap_secret[k], hashmap_guess[k])

        return '{}A{}B'.format(bull_count, cow_count)
