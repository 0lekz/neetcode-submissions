class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        flag = 0
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                if flag:
                    return False

                flag += 1
                return (isPalindrome(left + 1, right) or isPalindrome(left, right - 1))
                
            left += 1
            right -= 1
        return True
            
            
                