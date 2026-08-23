class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers move from ends to middle
        # max = area of greatest position 
        # shorter height pointer takes a step in
        # while pointer index 1 != pointer index 2 

        left, right = 0, len(heights)-1
        area = 0

        while left != right:
            curr = min(heights[left], heights[right]) * (right - left)
            if (curr > area):
                area = curr
            if (heights[right] > heights[left]):
                left += 1
            else: 
                right -=1

        return area