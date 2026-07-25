class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in hash:
                return [hash[goal], i]
            else:
                hash[nums[i]] = i
