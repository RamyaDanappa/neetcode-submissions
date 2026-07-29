class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        current_height = 0

        l=0
        r=len(heights)-1

        while l<r:
            current_height= min(heights[l], heights[r])
            width = r-l

            max_area=max(max_area, current_height*width)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_area



        