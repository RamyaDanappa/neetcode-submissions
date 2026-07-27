class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset =set(nums)
        longest =0
        for n in nums:
            if (n-1) not in numset:
                res =0
                while (n+res) in numset:
                    res+=1
                longest= max(res,longest)
        return longest
            

        