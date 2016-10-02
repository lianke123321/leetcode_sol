# no Liana solution


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for s in strings:
            if len(s) == 1:
                if '-1' not in hashmap:
                    hashmap['-1'] = [s]
                else:
                    hashmap['-1'].append(s)
            else:
                key = ' '.join([self.get_distance(s[i], s[i + 1]) for i in xrange(len(s) - 1)])
                if key in hashmap:
                    hashmap[key].append(s)
                else:
                    hashmap[key] = [s]

        return [hashmap[i] for i in hashmap]

    def get_distance(self, a, b):
        diff = ord(b.upper()) - ord(a.upper())
        return str(diff) if diff >= 0 else str(26 + diff)
