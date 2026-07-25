from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counted =Counter(nums)
    
        for k,v in counted.items():
            
            if v>1:
                return True
        return False
        