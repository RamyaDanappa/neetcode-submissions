from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for s in strs:
            key=''.join(sorted(s))
            temp[key].append(s)
        return list(temp.values())
        