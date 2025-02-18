from typing import List


class Solution:

  def encode(self, strs: List[str]) -> str:
    res = ""
    for s in strs:
      res += str(len(s)) + "#" + s # add the length of the string followed by # and the string
    return res


  def decode(self, s: str) -> List[str]:
    res = []
    i = 0

    while i < len(s): # iterate through the string
      j = i
      while s[j] != '#': # loop until you find a #
        j += 1 # increment the pointer
      length = int(s[i:j]) # get the length of the string
      i = j + 1
      j = i + length # get the end of the string
      res.append(s[i:j]) # add the string to the result
      i = j # increment the pointer to start of the next string

    return res

solution = Solution()
print(solution.encode(["we","say","#","yes"]))
print(solution.decode('2#we3#say1##3#yes'))