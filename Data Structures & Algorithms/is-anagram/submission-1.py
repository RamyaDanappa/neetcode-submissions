from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(s)
        t_map = Counter(t)

        if len(s) != len(t) or len(s_map) != len(t_map):
            return False
        
        for k,v in s_map.items():
            if t_map[k]!=v:
                return False
        return True


        