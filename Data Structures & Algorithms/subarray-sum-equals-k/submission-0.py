class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        prefix_sums = {0: 1}
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        return count
