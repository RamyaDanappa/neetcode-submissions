class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        if not nums:
            return [[]]
        def helper(nums, slate, target, i, res):
            #base
            if target==sum(slate):
                    res.append(slate[:])
                    return
            if i>=len(nums): 
                return
            #recursion
            #exclude
            helper(nums, slate, target, i+1, res)
            #include
            if sum(slate) + nums[i] <= target:
                slate.append(nums[i])
                helper(nums, slate, target, i, res)
                slate.pop()
        helper(nums, [],target, 0, res)
        return res

        