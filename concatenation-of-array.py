from typing import List


class Solution:
  def getConcatenation(self, nums: List[int]) -> List[int]:
    ans = []
    x = 2 # no of times to concatenate the array
    for i in range(x): # append the new array by x or 2 times
      for num in nums:
        ans.append(num)

    return ans

solution = Solution()
print(solution.getConcatenation([1,2,1]))