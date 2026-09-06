class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        left = 0

        window_sum = sum(arr[:k])

        for right in range(k, len(arr) + 1):

            # Check current window
            if window_sum / k >= threshold:
                count += 1

            # Move window
            if right < len(arr):
                window_sum -= arr[left]
                window_sum += arr[right]
                left += 1

        return count