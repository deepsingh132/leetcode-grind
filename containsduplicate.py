from typing import List


class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums) # if the set is not equal to nums then duplicate(s) exist


solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))