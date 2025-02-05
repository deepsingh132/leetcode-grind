from typing import List
class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        np = sorted(nums) # sort the array
        return np[n//2] # return the middle element of the sorted array (the majority element)

solution = Solution()
print(solution.majorityElement([3,2,3]))