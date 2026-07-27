class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =[]
        for s in strs:
            found =False
            for r in res:
                if Counter(s)==Counter(r[0]):
                    found= True
                    r.append(s)
                    break
            if found ==False:
                res.append([s])
                
        return res