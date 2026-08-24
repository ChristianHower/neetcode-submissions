class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # two pointers move towards middle
        # looking for goal number
        # if right num > goal + left num, move right down. 
        # once hit that, move left up 1. 

        left, right = 0, len(numbers) - 1

        while True:
            goal = target - numbers[left]
            if numbers[right] > goal:
                right -= 1
            elif numbers[right] < goal:
                left += 1
            else:
                return [left + 1, right + 1]