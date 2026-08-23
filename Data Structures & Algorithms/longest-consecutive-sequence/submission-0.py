class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of nums
        numss = set(nums)

        Max = 0

        # for each num in nums, check highest set sequence.
        for n in range(len(nums)):
            curr = 1
            while (nums[n] + curr) in numss:
                curr += 1
            # if > max, max = curr
            if curr > Max:
                Max = curr

        return Max