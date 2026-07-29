class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use monotonic decreasing stack (temp, index) pairs
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][0]:
                prev_t, prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append((t, i))

        return result