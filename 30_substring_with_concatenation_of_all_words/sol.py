class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        length = len(s)
        count = len(words)
        if length <= 0 or count <= 0:
            return result
        hashMap = {}
        for i in range(count):
            if words[i] not in hashMap:
                hashMap[words[i]] = 1
            else:
                hashMap[words[i]] += 1
        k = len(words[0])
        for i in range(k):
            left = i
            n = 0
            tempMap = {}
            j = i
            while j <= length - k:
                t = s[j: j + k]
                if t in hashMap and hashMap[t] > 0:
                    if t not in tempMap:
                        tempMap[t] = 1
                    else:
                        tempMap[t] += 1
                    if tempMap[t] <= hashMap[t]:
                        n += 1
                    else:
                        while(tempMap[t] > hashMap[t]):
                            t1 = s[left: left + k]
                            tempMap[t1] -= 1
                            if tempMap[t1] < hashMap[t1]:
                                n -= 1
                            left += k
                    if n == count:
                        result.append(left)
                        tempMap[s[left: left + k]] -= 1
                        n -= 1
                        left += k
                else:
                    tempMap = {}
                    n = 0
                    left = j + k
                j += k
        return result

    def findSubstring_self(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        hashmap = {}
        result = []
        num_of_words = len(words)
        len_of_word = len(words[0])

        if len(s) < num_of_words * len_of_word:
            return result

        for word in words:
            hashmap[word] = hashmap[word] + 1 if word in hashmap else 1

        # there are only len_of_word num of iterations we need
        # to count through the s
        for i in range(len_of_word):
            start = i  # log the start of current count
            j = i  # j is the current pointer to next word
            tmp = {}  # hashmap for this iteration
            n = 0  # number of matched words so far
            while j <= len(s) - len_of_word:
                curr_word = s[j:j+len_of_word]
                if curr_word not in hashmap:
                    n = 0
                    tmp = {}
                    start = j + len_of_word
                else:
                    tmp[curr_word] = tmp[curr_word] + 1 if curr_word in tmp else 1
                    if tmp[curr_word] <= hashmap[curr_word]:
                        n += 1
                    else:
                        while tmp[curr_word] > hashmap[curr_word]:
                            del_word = s[start:start+len_of_word]
                            tmp[del_word] -= 1
                            if tmp[del_word] < hashmap[del_word]:
                                n -= 1
                            start += len_of_word

                    if n == num_of_words:
                        result.append(start)
                        tmp[s[start:start+len_of_word]] -= 1
                        start += len_of_word
                        n -= 1

                j += len_of_word
        return result


sol = Solution()
print sol.findSubstring_self("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])
