class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # within days days so from 0 to days. 

        # minimun capacity has to be at least weights 

        # so we can search for capacity given number of days. And we know min capacity
        # Brute force approach would be to simulate delivery for each capacity starting from
        # initial and going +1 if it doesn't work. 

        def canShip(capacity):
            ships = 1
            currCap = capacity  
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap = currCap - w
            return True

        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res