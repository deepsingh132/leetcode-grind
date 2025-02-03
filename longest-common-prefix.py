from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]  # Start with the first string as the prefix

        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]  # Reduce the prefix by one character
                if not prefix:  # If the prefix becomes empty, no common prefix exists
                    return ""

        return prefix


solution = Solution()
print(solution.longestCommonPrefix(["hello","hellish","helmet"]))