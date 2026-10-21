class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # the idea 
        def hm(s: str):
            count = {}
            for i in range(len(s)):
                count[s[i]] = 1 + count.get(s[i], 0)
            return count

        if len(s1) > len(s2):
            return False

        s1count = hm(s1)
        l = 0
        r = l + len(s1)

        # compute first hashmap for substring
        substring = s2[l:r]
        scount = hm(substring)

        while True:
            if s1count == scount:
                return True

            if r == len(s2):
                return False

            # remove the outgoing character
            outgoing = s2[l]
            scount[outgoing] -= 1
            if scount[outgoing] == 0:
                del scount[outgoing]

            # add the incoming character
            incoming = s2[r]
            scount[incoming] = 1 + scount.get(incoming, 0)

            l += 1
            r += 1