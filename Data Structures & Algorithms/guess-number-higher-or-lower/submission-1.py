# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        def binary_helper(start,end):
            while start <= end:
                mid = (start + end)//2

                if guess(mid)>0:
                    start = mid+1
                elif guess(mid)<0:
                    end = mid -1
                else:
                    return mid
            return -1
        return binary_helper(1, n)