class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left =0
        window=[nums[0]]

        for right in range(1,len(nums)):
            if right-left>k:
                window.remove(nums[left])
                left+=1
            if nums[right] in window:
                return True
            else:
                window.append(nums[right])
        return False

            
        