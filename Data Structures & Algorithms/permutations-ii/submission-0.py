class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res =[]
        
        def helper(nums, slate, res,i):
            if len(nums)==i:
                res.append(slate[:])
                return
            repeat=set()
            for j in range(i, len(nums)):
                
                if nums[j] in repeat:
                    continue

                repeat.add(nums[j])
                nums[i],nums[j]=nums[j],nums[i]
                slate.append(nums[i])
                helper(nums, slate, res, i+1)
                slate.pop()
                nums[i],nums[j]=nums[j],nums[i]
        helper(nums, [], res, 0)
        return res
        