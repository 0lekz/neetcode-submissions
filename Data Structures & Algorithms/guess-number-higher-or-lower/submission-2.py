# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L, R = 1, n
        
        while True:
            m1 = L + (R - L) // 3
            m2 = R + (R - L) // 3
            
            if guess(m1) == 0:
                return m1
            if guess(m2) == 0:
                return m2

            if guess(m1) + guess(m2) == 0:
                # correct number is in-between m1 and m2
                L = m1 + 1
                R = m2 - 1

            elif guess(m1) == -1:
                # correct number is lower than m1
                R = m1 - 1
            else:
                # correct number is higher than m2
                L = m2 + 1