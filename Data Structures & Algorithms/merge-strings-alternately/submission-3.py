class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_size, w2_size = len(word1), len(word2)
        i = 0
        res = []

        while i < w1_size or i < w2_size:
            if i < w1_size: res.append(word1[i])
            if i < w2_size: res.append(word2[i])
            i += 1

        return "".join(res)