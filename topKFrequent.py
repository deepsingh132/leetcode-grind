from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using modified bucket sort
        count = {} # create a hashmap
        freq = [[] for i in range(len(nums) + 1)] # create an empty array

        for n in nums: # iterate through the array
            count[n] = 1 + count.get(n, 0) # increment the count of the number
        for n, c in count.items(): # iterate through the count hashmap
            freq[c].append(n) # add the number to the frequency array

        res = []
        for i in range(len(freq) -1, 0 ,-1): # iterate through the frequency array in descending order
            for n in freq[i]:
                res.append(n) # add the number to the result
                if len(res) == k: # if the result is equal to k return the result
                    return res

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))