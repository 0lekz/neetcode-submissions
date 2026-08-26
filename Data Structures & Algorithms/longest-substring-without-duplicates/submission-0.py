class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest sequence without duplicate chars,
        # so basically a longest sequence of unique chars
        if len(s) <= 1:
            return len(s)

        right = 1
        left = 0
        res = 0
        hashset = set()
        hashset.add(s[left])
        while right < len(s):
            if s[right] in hashset:
                while s[right] in hashset:
                    hashset.remove(s[left])
                    left += 1
            if res <= right - left + 1:
                res = right - left + 1
            
            hashset.add(s[right])
            right += 1
        
        return res        
                    
              
             

