class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr)<k:
            return None
        count =0
        window = sum(arr[:k])
        if window / k >= threshold:
            count += 1
        
        for i in range(k, len(arr)):
            window+=arr[i]-arr[i-k]
            if window/k >=threshold:
                count+=1
        return count
            
        
        