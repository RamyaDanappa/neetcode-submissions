from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp=Counter(nums)
        temp_heap =[]

        for key,val in temp.items():
            heapq.heappush(temp_heap,(-val, key))
        res =[]
        for i in range(k):
            _,num = heapq.heappop(temp_heap)
            res.append(num)
        return res

        