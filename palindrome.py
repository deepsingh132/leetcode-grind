class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x) # Typecasting x to string
        return st[:] == st[::-1] #  check if st is equal to it's reverse and return

solution = Solution()
print(solution.isPalindrome(12121))