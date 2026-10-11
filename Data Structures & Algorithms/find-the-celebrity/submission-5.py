# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0 
        for i in range(1,n):
            if knows(candidate, i) ==  True:
                candidate=i
        
        for j in range(n):
            if j != candidate:
                if knows(candidate, j) == True or knows(j, candidate) != True:
                    return -1
        return candidate
        