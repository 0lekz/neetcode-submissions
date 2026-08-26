class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""

        for idx in range(len(strs[0])):
            char = strs[0][idx]

            for s in strs[1:]:
                if idx >= len(s) or s[idx] != char:
                    return strs[0][:idx]

        return strs[0]