class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1=-1
        i2=-1
        min_distance= math.inf
        for i in range(len(wordsDict)):
            if word1== wordsDict[i]:
                i1=i
            if word2== wordsDict[i]:
                i2=i
            
            if i1!=-1 and i2!=-1:
                min_distance= min(min_distance, abs(i1-i2))
        return int(min_distance)
        