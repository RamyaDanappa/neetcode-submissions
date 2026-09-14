class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def helper(slate, i,n,k):
            #base

            if k==len(slate) and slate not in res:
                res.append(slate[:]) 
            if i==n:
                return

            #exclude
            helper(slate, i+1, n,k)
            #include
            slate.append(i+1)
            helper(slate,i+1, n,k)
            slate.pop()
        helper([],0,n,k)
        return res       