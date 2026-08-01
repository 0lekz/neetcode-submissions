class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # since python has dynamic arrays right away we just append:
        ans = nums

        for i in range(len(nums)):
            ans.append(ans[i])

        return ans

