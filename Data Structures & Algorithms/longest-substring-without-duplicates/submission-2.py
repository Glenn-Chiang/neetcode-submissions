class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        charSet = set()
        i = 0
        for j in range(len(s)):
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1
            charSet.add(s[j])
            maxLength = max(maxLength, j - i + 1)
        return maxLength

