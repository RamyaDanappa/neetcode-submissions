class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        temp=[]

        for num in nums:
            heapq.heappush(temp, -num)
        res =0
        for _ in range(k):
            res = -(heapq.heappop(temp))
        return res

        