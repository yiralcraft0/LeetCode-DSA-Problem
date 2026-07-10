'''
14. Longest Common Prefix
Easy

->
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:----------
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:-----------
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    # Optimised Way solutions---------------------------
    # time complexity: O(n)

    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return prefix
            prefix += first[i]
    
        return prefix            


strs = ["aaa", "aa","a", "aaa"]

solve = Solution()

print(f"{solve.longestCommonPrefix(strs)}")