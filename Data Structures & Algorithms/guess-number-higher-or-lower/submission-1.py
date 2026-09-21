# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        L = 1
        R = n

        while True: 
            pick = (L + R) // 2
            res = guess(pick)

            if res == 0:
                # correct guess
                return pick

            if res == -1:
                # my guess is higher
                R = pick - 1
            
            if res == 1:
                # my guess is lower
                L = pick + 1

