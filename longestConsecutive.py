from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # create a set of nums
        longest = 0

        for num in numSet: # iterate through the set
            if (num - 1) not in numSet: # if the number is not in the set then it is the start of a sequence
                length = 1 # set the length to 1
                while (num + length) in numSet: # loop while current number + length is in the set
                    length += 1 # increment the length
                longest = max(length, longest) # update the longest
        return longest

solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))