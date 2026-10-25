class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_area = self.compute_area(heights, left, right)
        while right>(left+1):
            if heights[right]<heights[left]:
                right -= 1
                area_right = self.compute_area(heights, left, right)
                max_area = max(area_right, max_area)
            else:
                left += 1
                area_left = self.compute_area(heights, left, right)
                max_area = max(area_left, max_area)
        return max_area
            
    @staticmethod
    def compute_area(heights, i, j):
        return min(heights[i], heights[j]) * (j-i)