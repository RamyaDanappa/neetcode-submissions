class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n <0:
            x=1/x
            n=-n
        
        def dfs(n):
            if n==0:
                return 1
            
            half= dfs(n//2)

            if n%2==0:
                #even
                return half * half
            else:
                #odd 
                return half *half * x

        
        return dfs(n)

        