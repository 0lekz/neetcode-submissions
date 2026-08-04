class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need to find the maximum difference between some
        # prices[i] and prices[j], where j > i and
        # prices[j] >= prices[i], 
        # with edge case when array sorted descending

        ret, idx = 0, 0
        # brute force solution is to compare every prices[i]
        # with every subsequent prices[j] so n^2 time complexity

        # since when finding out that the difference between
        # prices[i] and prices[j] is >= 0 it's always better to
        # select prices[j] as the buy candidate, 
        # since it's cheaper (or equal)
        # in case prices[i] < prices[j] we it means so prices[i]
        # is a better option to choose, and we keep searching
        # prices[j+1] in case prices[j+1] < prices[i]

        for i in range(1, len(prices)):
            if prices[idx] >= prices[i]:
                idx = i
            else: # prices[idx] < prices[i]
                temp = prices[i] - prices[idx]
                if temp > ret:
                    ret = temp
                else:
                    continue
        return ret