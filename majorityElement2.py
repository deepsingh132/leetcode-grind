from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # using Boyer-Moore Voting Algorithm (Hashmap)
        count = defaultdict(int)

        for n in nums:
            count[n] += 1 # add the number to the count hashmap

            if len(count) <= 2: # if the count is less than or equal to 2 then continue
                continue

            new_count = defaultdict(int) # create a new count hashmap
            for n, c in count.items(): # iterate through the count hashmap
                if c > 1: # if the count is greater than 1
                    new_count[n] = c - 1 # subtract 1 from the count and add the number to the new count
            count = new_count

        res = []
        for n in count: # iterate through the count
            if nums.count(n) > len(nums) // 3: # if the count is greater than the length of the array divided by 3 then add the number to the result
                res.append(n)
        return res

solution = Solution()
print(solution.majorityElement([3,2,3]))