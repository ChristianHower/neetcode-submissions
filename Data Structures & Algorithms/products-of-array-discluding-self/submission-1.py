class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res, left, right = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        for n in range(len(nums) - 1): 
            left[n + 1] = left[n]
            left[n + 1] *= nums[n]
            right[len(nums) - 2 - n] = right[len(nums) - 1 - n]
            right[len(nums) - 2 - n] *= nums[len(nums) - 1 - n]
        
        res = [x * y for x, y in zip(left, right)]

        return res
