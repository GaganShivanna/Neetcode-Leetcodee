class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def signature(words):
            count = [0] * 26
            for c in words:
                count[ord(c) - ord('a')] += 1
            return tuple(count)
        res = [words[0]]
        prev_sign = signature(words[0])

        for i in range(1, len(words)):
            curr_sign = signature(words[i])
            if curr_sign != prev_sign: 
                res.append(words[i])
                prev_sign = curr_sign 
        return res 