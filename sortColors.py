from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r=0, len(nums)-1
        i=0

        def swap(i,j): # swap function
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0: # if the number is 0 then swap it with the left pointer
                swap(l, i)
                l+= 1

            elif nums[i] == 2: # if the number is 2 then swap it with the right pointer
                swap(i,r)
                r-= 1
                i-= 1
            i+= 1


solution = Solution()
print(solution.sortColors([2,0,2,1,1,0]))