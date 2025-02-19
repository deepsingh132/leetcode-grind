from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # create an array of ones

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix # add the prefix to the result
            prefix *= nums[i] # multiply the prefix by the current number
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # iterate through the array in reverse
            res[i] *= postfix # multiply the result by the postfix
            postfix *= nums[i] # multiply the postfix by the current number

        return res

solution = Solution()
print(solution.productExceptSelf([1, 2, 4, 6]))