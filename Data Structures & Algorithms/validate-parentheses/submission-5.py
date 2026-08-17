class Solution:
    def isValid(self, s: str) -> bool:
        barkets={
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack =[]

        for ch in s:
            if ch in barkets:
                if stack and stack[-1]==barkets[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return not stack
