from typing import List


class Solution:
  def removeElement(self, nums: List[int], val: int):
    i=0
    for j in range(len(nums)):
      if nums[j] != val:
        nums[i], nums[j] = nums[j], nums[i] # swap the values
        i += 1
    return i # return the count of elements not equal to val

solution = Solution()
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))