class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_pos_start():
            left =0
            right =len(nums)-1
            start =-1

            while left<=right:
                mid = (left+right)//2
                if nums[mid] == target:
                    start = mid
                    right= mid-1
                elif nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            return start
        def find_pos_end():
            left =0
            right =len(nums)-1
            end =-1

            while left<=right:
                mid = (left+right)//2
                if nums[mid] == target:
                    end = mid
                    left= mid+1
                elif nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            return end
        return [find_pos_start(),find_pos_end()]


        