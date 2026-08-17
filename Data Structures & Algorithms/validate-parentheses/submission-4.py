class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                res.append(ch)

            elif ch == ")":
                if not res or res.pop() != "(":
                    return False

            elif ch == "}":
                if not res or res.pop() != "{":
                    return False

            elif ch == "]":
                if not res or res.pop() != "[":
                    return False

        return len(res) == 0