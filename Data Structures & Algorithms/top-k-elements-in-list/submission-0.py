class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # put list in order
        nums.sort()

        # create hashmap of all nums with their counts
        hash = {}
        count = 0

        for i in range(len(nums)):
            if i > 0 and nums[i-1] != nums[i]:
                hash[nums[i-1]] = count
                count = 0
            count += 1
        hash[nums[i-1]] = count

        # k times, add hashmap key with greatest value, then remove the pair from og hashmap
        final =[]
        for j in range(k):
            final.append(max(hash, key=hash.get))
            hash.pop(max(hash, key=hash.get))

        # return final list
        return(final)