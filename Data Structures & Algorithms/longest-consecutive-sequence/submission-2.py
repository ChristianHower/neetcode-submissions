class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of nums
        numss = set(nums)

        Max = 0

        # for each num in nums, check highest set sequence.
        for n in nums:
            if n - 1 not in numss:
                curr = 1
                while (n + curr) in numss:
                    curr += 1
                # if > max, max = curr
                Max = max(Max, curr)

        return Max