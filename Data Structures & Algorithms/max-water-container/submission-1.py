class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = 0

        while i < j:
            width = j - i
            if heights[i] < heights[j]:
                minheight = heights[i]
                i += 1
            else:
                minheight = heights[j]
                j -= 1
            maxArea = max(maxArea, minheight * width)
        
        return maxArea
