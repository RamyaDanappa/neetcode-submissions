class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp={}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff not in temp:
                temp[nums[i]] =i
            else:
                return [temp[diff], i]
        return [-1,-1]
