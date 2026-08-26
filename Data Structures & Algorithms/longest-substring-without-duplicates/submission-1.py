class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest sequence without duplicate chars,
        # so basically a longest sequence of unique chars
        if len(s) <= 1:
            return len(s)

        mp = {}
        left = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                left = max(mp[s[r]] + 1, left)
            mp[s[r]] = r
            res = max(res, r - left + 1)

        return res        
                    
              
             

