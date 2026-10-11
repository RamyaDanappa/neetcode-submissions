# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0

        # Step 1: Find a possible celebrity
        for i in range(1, n):
            if knows(candidate, i)== True:
                candidate = i

        # Step 2: Verify the candidate
        for i in range(n):
            if i == candidate:
                continue

            if knows(candidate, i) == True or knows(i, candidate) != True:
                return -1

        return candidate