class Solution:
    def isValid(self, s: str) -> bool:
        # first solution that comes to mind is to use 3 counters. Since we know we need to keep track of
        # '()' '{}' and '[]', simply the amount of '(' has to match the amount of ')' (alternative signs, sum is 0)
        # but that solution fails when we have something like '())(', since count is correct but fails point 2; 

        # with similar logic, and considering that the question is under category of stacks. We can use a stacks to track
        # essentially the same logic, but now we add '(' when we see it, and pop one when we see ')',
        
        # thus if stack empty and we trying to pop - return false, if stack not empty at the end of the program - return false

        # does python have stack type? I think append pop might work?

        # it's actually much easier now that I see counter example. since "[(])" is not a valid string. Thus only one stack needed.

        """
        valid parentheses must follow a last-opened, first-closed order. So we use a stack
        Whever we see a closing bracket, simply check whether it mathces the most recent opening bracket on top of the stack/
        If matches, we can remove that opening bracket.
        If it doesn't, or we trying to remove from empty string - return false.
        Valid string ends up with an empty stack.
        If not empty - return false.
        """

        bracket = []

        # could map better than elifs with:
        closeToOpen = { ")": "(", "]": "[", "}": "{"}

        for c in s: 
            if c in closeToOpen:
                try:
                    last = bracket.pop()
                except IndexError:
                    return False
                if last != closeToOpen[c]:
                    return False
            else:
                bracket.append(c)
            
        return False if len(bracket) > 0 else True
            
            