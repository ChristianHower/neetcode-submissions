class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) > 1:
            hash = {}
            for i in range(len(nums)):
                if nums[i] in hash:
                    return True
                hash[nums[i]] = i
        return False