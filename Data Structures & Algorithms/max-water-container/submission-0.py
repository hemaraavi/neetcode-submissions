class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = min(left_height,right_height) * (right_index - left_index)
        l ,r = 0 , len(heights)-1
        max_area = 0
        while l<r:
            area = min(heights[l],heights[r]) * (r - l)
            if area >max_area:
                max_area = area
            if heights[l] < heights[r]:
                l= l+1
            else:
                r = r-1
        return max_area
            
