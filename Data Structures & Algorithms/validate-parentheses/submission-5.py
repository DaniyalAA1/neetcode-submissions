class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching = {')' : '(', '}' : '{', ']' : '['}
        for i in range(len(s)):
            if s[i] in matching.values():
                stack.append(s[i])
                # closing bracket has to be the key for python dict one way lookup
                # if its an opening bracket, push it onto the stack
                #checking opening first since we read chronologically left to right
            elif s[i] in matching:
                expected_opening = matching[s[i]]
                if stack and stack[-1] == expected_opening:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

        