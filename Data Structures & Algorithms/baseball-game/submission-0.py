class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for val in operations:
            if val == '+':
                res.append(res[-1]+res[-2])
            elif val =='D':
                res.append(res[-1]*2)
            elif val=='C':
                res.pop()
            else:
                res.append(int(val))
        return sum(res)
        