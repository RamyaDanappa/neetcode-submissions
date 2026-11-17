class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =[]
        temp={}
        for s in strs:
            key = "".join(sorted(s))
            if key  in temp:
                temp[key].append(s)
            else:
                temp[key]=[s]
        return list(temp.values())