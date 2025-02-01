from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if num in map: # lookup current num
                return [map[num],i]
            # will find complement at index i
            map[complement] = i

        return []

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))