class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr_len =len(nums)
        ans = [-1]*(2*arr_len)
        for i in range(arr_len):
            ans[i] = nums[i]
            ans[i+arr_len]= nums[i]
           
        return ans
        