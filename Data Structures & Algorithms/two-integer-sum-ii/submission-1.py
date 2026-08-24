class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}

        for n in range(len(numbers)):
            goal = target - numbers[n]
            if goal in hashMap:
                return [hashMap[goal] + 1, n + 1]
            hashMap [numbers[n]] = n