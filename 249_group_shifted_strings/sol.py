# no Liana solution


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        result = []
        hashmap = {}
        for s in strings:
            if len(s) == 1:
                if '-1' not in hashmap:
                    hashmap['-1'] = [s]
                else:
                    hashmap['-1'].append(s)
            else:
                tmp = []
                for i in range(len(s) - 1):
                    tmp.append(self.get_distance(s[i], s[i + 1]))
                key = ' '.join(tmp)
                if key in hashmap:
                    hashmap[key].append(s)
                else:
                    hashmap[key] = [s]

        for k in hashmap:
            result.append(hashmap[k])
        return result

    def get_distance(self, a, b):
        d1, d2 = ord(a.upper()), ord(b.upper())
        if d2 >= d1:
            return str(d2 - d1)
        else:
            return str(26 - abs(d2 - d1))
