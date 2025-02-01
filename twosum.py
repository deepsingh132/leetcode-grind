from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if num in hashmap: # lookup current num in hashmap
                return [hashmap[num],i]
            # store the complement and its index
            hashmap[complement] = i

        return []

solution = Solution()
print(solution.twoSum([3,2,4], 6))