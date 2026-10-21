class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #
        def hm(s: str):
            count = {}
            for i in range(len(s)):
                count[s[i]] = 1 + count.get(s[i], 0)
            return count

        s1count = hm(s1)

        l = 0
        r = l + len(s1)

        while r <= len(s2):
            substring = s2[l:r]
            scount = hm(substring)

            if s1count == scount:
                return True
            
            l += 1
            r += 1

        return False