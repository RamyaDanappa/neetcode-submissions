
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_size =0
        count =0 
        i=0
        for j in range(len(nums)):
            if nums[j]==0:
                count+=1
            if count>k:
                if nums[i]==0:
                    count-=1
                i+=1
            max_size= max(max_size,j-i+1)
        return max_size


            
        