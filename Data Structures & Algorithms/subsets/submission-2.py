class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res=[]
        def helper(slate, nums,res, i):
            #base
            if i==len(nums):
                res.append(slate[:])
                return
            #recursion
            #1type exclude:
            helper(slate, nums, res, i+1)
            #2 type include:
            slate.append(nums[i])
            helper(slate, nums, res,i+1)
            slate.pop()
        helper([], nums, res, 0)
        return res

            