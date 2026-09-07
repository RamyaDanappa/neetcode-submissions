from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count=Counter(s1)
        k=len(s1)

        for i in range(len(s2)):
            if s1_count==Counter(s2[i:i+k]):
                return True
        return False        
        