class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
                elif len(stack) == 1:
                    stack.append(stack[-1])
                else:
                    continue
            elif op == 'C':
                if stack:
                    stack.pop()
                else:
                    continue
            elif op == 'D':
                if stack:
                    stack.append(stack[-1] * 2)
                else: continue
            else:
                stack.append(int(op))

        return sum(stack)
            
