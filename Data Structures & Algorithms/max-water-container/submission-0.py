class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # slow fast pointers
        # slow points at current max left value
        # fast moves and checks if value to the right would make the area larger 
        # that's it? 

        left, right = 0, 1

        mMax = min(heights[left], heights[right]) * (right-left)
        for i in range(len(heights)):
            curr = min(heights[left], heights[i]) * (i-left)
            if curr > mMax:
                mMax = curr
                left = right
        
        return mMax

        