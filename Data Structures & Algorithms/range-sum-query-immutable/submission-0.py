class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.res =[]

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        print(sum(self.nums[left:right+1]))
        total = sum(self.nums[left:right+1])
        self.res.append(total)
        return total



        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)